# Nodejs 아키텍처
- Nodejs는 **싱글 스레드, 논 블로킹** 이라고 한다.
- 하나의 스레드로 동작하지만 I/O 작업이 발생한 경우 이를 **비동기적**으로 처리 할 수 있다.
- 비동기 작업을 블로킹 없이 수행 할 수 있는데, 그 기반에는 **이벤트 루프**가 존재한다.
![Nodejs의 구조](https://www.korecmblog.com/static/96ae7fa015e5e34fb42e0aa5c34a13e2/bfc0a/1*yEW6321eqBd_-C0D7LsBQw.webp)
## libuv
![libuv](https://www.korecmblog.com/static/3c245619710623f6c5d916f7271c414a/a9a89/banner.webp)
- libuv란 C++로 작성된, Node.js가 사용하는 비동기I/O 라이브러리 이다.
- 운영체제의 커널을 추상화한 Wrapping 라이브러리로 커널이 어떤 비동기 API를 지원하는지 알고 있다.
![동작구조](https://www.korecmblog.com/static/e14c952554120cfccf77d21be8827196/e5c51/libuv-%EC%BB%A4%EB%84%90.webp)
- 비동기 작업을 요청하면 libuv는 이 작업을 커널이 지원하는지 확인한다.
- 작업이 지원한다면 libuv가 대신 커널에 **비동기적으로 요청했다가 응답이 오면 그 응답**을 우리에게 전달해준다.
- 작업이 지원하지 않는다면 자신만의 **워커 스레드**가 담긴 스레드 풀을 사용한다.
![동작구조2](https://www.korecmblog.com/static/f86a212e43d4313a41339ef5f86e4a6c/e5c51/libuv-%EC%9B%8C%EC%BB%A4-%EC%8A%A4%EB%A0%88%EB%93%9C-1.webp)
- libuv는 기본적으로 4개의 스레드를 가지는 스레드 풀을 생성한다.
- 최대 128개 까지 스레드 개수를 늘릴수 있다. 아래 변경법 확인
- 요청한 작업을 **커널**이 지원하지 않는다면 libuv는 커널을 호출하는 대신 스레드 풀에게 작업을 맡겨버린다.
``` javascrpit
process.env.UV_TRHEADPOOL = 4; // 스레드 풀 개수를 지정해줄 수 있다.
```

## libuv와 이벤트 루프
![eventloop](https://www.korecmblog.com/static/2dcc70f2d6c5e3f8d2dae0179a149283/e5c51/event-loop.webp)
- Node.js는 I/O 작업을 자신의 메인 스레드가 아닌 다른 스레드에 위임함으로써 싱글 스레드로 논 블로킹 I/O를 지원한다.
- 다르게 말하면 Node.js는 I/O작업을 libuv에게 위임함으로써 논 블로킹 I/O를 지원하고 그 기반에는 **이벤트루프**가 있다.
``` javascrpit
file.readFile('test.txt', callback)
```
- 위와 같은 비동기 작업을 모아서 순서대로 실행 할 수 있게 도와주는 도구이며 위의 그림과 같이 구성되어있다.
- 각 **박스**는 특정 작업을 수행하기 위한 **페이즈(Phase)**를 의미한다. 그리고 Node.js의 이벤트 루프는
- Phase의 실행 순서 (Timer Phase -> Pending Callbacks Phase -> Idle, Prepare Phase -> Poll Phase -> Check Phase -> Close Callbacks Phase -> Timer Phase)
- 한 페이즈에서 다음 페이즈로 넘어가는 것을 **틱(Tick)**이라고 부른다.
- 각 페이즈는 자신만의 큐를 하나씩 가지고 있는데, 이 큐에는 이벤트 루프가 실행해야하는 작업들을 순서대로 가지고 있다.
- Node.js가 페이즈에 진입하면 이 큐에서 자바스크립트 코드를 꺼내서 하나씩 실행한다.
- 큐에있는 작업들을 다 실행하거나, 시스템의 실행 한도에 다다르면 Node.js는 다음 페이즈로 넘어간다.
- 이벤트 루프가 Node.js의 비동기 실행을 도와주는 것과 별개로 **싱글 스레드** 이므로 한번에 하나의 페이즈만 진입해 하나의 작업만 수행 할 수 있다.
- Poll Phase 작업을 처리하면서 Check Phase **작업을 동시에 처리 할 수 없다.**
``` c
int uv_run(uv_loop_t* loop, uv_run_mode mode) {
	// ...
  while (r != 0 && loop->stop_flag == 0) {
    uv__update_time(loop);
    uv__run_timers(loop);
    ran_pending = uv__run_pending(loop);
    uv__run_idle(loop);
    uv__run_prepare(loop);
    // ...
    uv__io_poll(loop, timeout);
	  // ...
    uv__run_check(loop);
    uv__run_closing_handles(loop);
	  // ...
    r = uv__loop_alive(loop);
    if (mode == UV_RUN_ONCE || mode == UV_RUN_NOWAIT)
      break;
  }
  return r;
}
```