# Chapter 07-01
# AsyncIO
# 비동기 I/O Coroutine 작업을 위한 패키지
# Generator -> 반복적인 객체 return 사용 (yield)
# None-Blocking 비동기 처리

# Blocking I/O : 호출된 함수가 자신의 작업이 완료 될 때까지 제어권을 가지고 있음, 타 함수는 대기
# None-Blocking I/O : 호출된 함수(서브루틴)가 Return (yield) 후 호출한(메인루틴) 함수에 제어권 전달 -> 타 함수 일 지속

# 스레드 단점 : 디버깅, 자원 접근 시 레이드 컨디션(경쟁 상태), 데드락(Dead Lock) 고려
# 코루틴 장점 : 하나의 루틴만 실행 -> 락 관리 필요 X -> 제어권으로 실행
# 코루틴 단점 : 사용 함수가 비동기로 구현되어 있어야한다. 

# block 함수를 AsyncIO를 이용해 사용하려면 Thread, Process를 함께 결합하여 사용하는 패턴 추천
import asyncio
import timeit
from urllib.request import urlopen # block 함수
from concurrent.futures import ThreadPoolExecutor
import threading

# 실행 시작 시간
st = timeit.default_timer()

# 서비스 방향이 비슷한 사이트 실습 권장
urls = ['http://daum.net', 'https://naver.com', 'http://mlbpark.donga.com', 'https://tistory.com', 'https://wemakeprice.com']

# fetch 함수 구현
async def fetch(url, executor):
    # 쓰레드명 출력
    print('Thread Name : ', threading.current_thread().getName(), 'Start', url)

    # 실행
    res = await loop.run_in_executor(executor, urlopen, url)
    print('Thread Name : ', threading.current_thread().getName(), 'Done', url)
    # 결과 반환
    return res.read()[:10]

# 비동기 함수
async def main():
    # 쓰레드 풀 생성
    executor = ThreadPoolExecutor(max_workers=10)

    # future 객체 모아서 gather에서 실행
    # url 1개당 1개의 thread를 사용해 비동기 식으로 처리
    futures = [
        asyncio.ensure_future(fetch(url, executor)) for url in urls
    ]

    # 결과 취합
    # await = yield
    result = await asyncio.gather(*futures) # unpacking

    print()
    print(result)

if __name__ == '__main__':
    # 루프 초기화
    loop = asyncio.get_event_loop()

    # main 함수 완료 까지 대기
    loop.run_until_complete(main())

    # 수행시간
    duration = timeit.default_timer() - st
    
    # 총 실행 시간
    print('Total Running Time : ', duration)
