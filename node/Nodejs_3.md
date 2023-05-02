## REPL
- 자바스크립트는 스크립트 언어이므로 미리 컴파일하지 않아도 즉석에서 코드를 실행 할 수 있습니다.
- 입력한 코드를 읽고, 해석하고, 결과물을 반환하고, 종료 할때까지 반복한다. REPL(Read Eval Print Loop) 라고 합니다.
```javascript
>  const str = "Hello word, hello node";
undefined
> console.log(str);
Hello World, hello node
undefined
```

## JS 파일 실행하기
- 실행할때 확장자는 생략가능
- node server.js

## 모듈로 만들기
- CommonJs, ECMAScript 모듈
- 특정하는 기능들의 집합을 만든다.
- 재활용이 가능
- node.js와 react 사용 해본바, node.js는 CommonJs를 사용 react는 ECMAScript 사용하는것을 보임.
- CommonJs는 표준 모듈이 아니지만 가장 널리 많이 쓰이는 모듈입니다.

### CommonJs
- 노드 생태계에서 가장 많이 쓴다.
- 함수와 변수도 가능하다.
- module.exports === exports 는 true
- require는 함수이다. ( 객체이다 )
```javascript

module.export = { odd, even };

...

const { odd, even } = require('./var'); // js는 생략가능, 구조분해 할당
```

### ECMAScript 모듈
- 공식적인 자바스크립트 모듈 형식
- ES 모듈이 표준으로 정해지면서 점점 ES 모듈을 사용 하는 비율이 늘어나고 있습니다.
- require, exports, module.exports는 각각 import, export, export deault로 바뀜
- 파일 확장자도 mjs로 변경되었음.
- js 확장자에서 import를 사용하여 에러 발생
```javascript
import { odd, even } from './var.mjs'

...

export default checkOddorEven;
```

### 정리
- CommonJs모듈과 ES 모듈을 알아봄, 서로 간에 잘 호환되지 않는 케이스들이 많으므로 한가지 형식만 사용하는 것을 권장

## 다이내믹 임포트
- 동적으로 모듈을 불러옴. ( 조건부 )
- import는 await이나 then을 붙혀서 사용하면 됨.

## __filename, __dirname
- filename : 파일 경로를 알 수 있음. ( 절대경로 )
- dirname : 디렉토리 경로를 알 수 있음. ( 절대경로 )

## 노드 내장 객체
- 노드프로그래밍 할때 많이 쓰는 내장 객체

### global
- 브라우저의 window와 같은 전역 객체이며, 전역 객체이므로 모든 파일에 접근 할 수 있습니다.
- global.message : 전역의 메세지를 넣을 수 있음.

### console
- 디버깅을 위해 로그, 개발중에 변수값이 제대로 들어 있는지 확인, time, error, table, dir, trace를 추가로 사용 할 수 있음.

### 타이머
- setTimeout : 주어진 밀리초 이후에 콜백 함수를 실행합니다.
- setInterval : 주어진 밀리초마다 콜백함수를 반복 실행합니다.
- setImmediate : 콜백함수를 즉시 실행합니다.
- clearTimeout(id) : setTimeout을 취소 (id값은 setTimeout 호출했을때 리턴되는 값 )
- clearinterval(id) : setInterval을 취소
- clearImmediate(id) : setImmediate를 취소

### Onvif 카메라 객체 내부 함수 중 5초마다 Connect 요청
```javascript
    start()
    {
        this.connect();
        this.interval = setInterval(() => {
            this.connect();
          }, 5000);
    }
```

```javascript
    stop()
    {
        clearInterval(this.interval);
    }
```

### process
- 프로세스 객체는 현재 실행되고 있는 노드 프로세스에 대한 정보를 담고 있습니다.
- 컴퓨터 정보를 알 수 있음
- process.env : 노드를 실행 할때 입력받는 환경변수들의 옵션들이 있는곳이다. ( 스레드 풀 조정 등...)
- process.nextTrik(콜백) :  이벤트 루프가 다른 콜백들 함수들 보다 nextTict 콜백함수를 우선 처리하도록 만듭니다.
- 마이크로태스크의 재귀 호출 : 다른 이벤트 루프에서 대기하는 콜백 함수보다 먼저 실행
- process.exit : 실행준인 노드 프로세스를 종료합니다.

### 기타 내장 객체
- AbortController, FormData, fetch, Headers, Requst, Response, Event, EventTarget : 브라우저에서 사용하던 AI가 노드에도 
- TextDecoder : Buffer를 문자열로 바꿉니다.
- TextEncoder : 문자열을 Buffer로 바꿉니다.
- WebAssembly : 웹어셉블리 처리를 담당합니다.


### 기타 추천 강의
- 코딩앙마 https://www.youtube.com/@codingangma - 자바스크립트, 리엑트
- Web Dev Simplified https://www.youtube.com/@WebDevSimplified - 자바스크립트, node express
