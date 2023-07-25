# 리액트
- 자바스크립트에 HTML을 포함하는 JSX(javascript XML)이라는 문법사용
- 가상 돔(Virtual DOM)이라는 개념을 사용하여 웹 어플레케이션의 퍼포먼스를 최적화함.
- 단방향 데이터 바인딩(One-way Data Binding) 사용
- 싱글 페이지 애플리케이션에서 UI를 만들기 떄문에 페이지 전환 기능을 사용하려면 react-router와 같은 추가 라이브러리를 사용해야함.
- 클라이언트 사이드 랜더링(CSR)

## 가상 돔(Virtual DOM)
- 리액트에서는 리플로우와 리액트가 자주 수행되는 문제를 해결하기 위해 화면에 표시되는 DOM과 동일한 DOM을 메모리상에 만들고 DOM 조작이 발생하면 메모리상에 생성된 가삼 돔에 모든 연산을 수행한 후, 실제 DOM을 갱신하여 리플로우/리패인트 연산을 최소화 한다.
- 리플로우(Reflow) : 레이아웃 구성을 다시 잡는다. (Layer Tree를 재구성한다)
- 리페인트(Repaint) : Reflow로 구성이 잡힌 이후에 그리는 작업
- 화면 구조가 변경된다면 Reflow와 Repaint가 모두 발생한다.

## 단방향 데이터 바인딩
- 단 하나의 Watcher가 자바스크립트의 데이터 갱신을 감지하여 사용자의 UI 데이터를 갱신합니다. 사용자가 UI를 통해 자바스크립트의 데이터를 갱신할 때는, 이벤트를 통해 갱신하게 됩니다. 이처럼 단방향 데이터 바인딩은 하나의 Watcher를 사용하기 때문에 양방향 데이터 바인딩이 가지는 성능적인 이슈를 해결하고 더 확실하게 데이터를 추적할 수 있게 해줍니다.

## 컴포넌트
- 화면에서 UI 요소를 구분할때 '컴포넌트' 라는 단위를 사용한다.
- 함수형 컴포넌트, 클래스 컴포넌트 2가지가 있다.
- 리액트에서 권장하는건 함수형 컴포넌트이다.

### 함수형 컴포넌트
- 함수형 컴포넌트는 함수형 기반 컴포넌트이다. return 문에 JSX 코드를 반환한다.
- 클래스형 컴포넌에 비해 함수형 컴포넌트가 비교적으로 메모리를 적게 사용한다.

### 클래스형 컴포넌트
- 클래스 기반 컴포넌트이고 render()함수에서 JSX코드를 반환한다.
- React의 ComponentClass를 상속받아 Component 상속이 필요하다.
- state, props, refs,컴포넌트 메서드, 생명주기 메서드를 사용할 때 this 로 프로퍼티를 참조하여 사용합니다.

## props
- 상위 컴포넌트가 하위 컴포넌트에 값을 전달할때 사용한다. ( 단방향 데이터 흐름을 갖는다.)
- 프로퍼티는 수정 할 수 없다는 특징이 있다.(하위 컴포턴넌트 입장에서는 읽기 전용 데이터이다.)
- 문자열전달할때 "", 변수를 전달할때 {} 를 사용한다.

## event
- 합성이벤트 : 모든 브라우저에 이벤트를 동일하기 처리하기 위하여 이벤트 레퍼를 전달받는데, 그 이벤트가 바로 합성이벤트이다.
- 고유이벤트 : 브라우저의 고유 이벤트
- event.preventDefault() : 기본동작을 막는다. ( 명시적으로 호출 해줘야함. )
- event.target : 이벤트를 유발 시킨 태그


## Hooks
 - 기본 Hooks : useState, useEffet, useContext
 - 추가 Hooks : useRedeuer, useCallback, useMemo, useRef ...
  
## state
- React의 Hook (useState)
- 이벤트에 의해 변경되는 동적인 값.
- state 값을 변경할때는 반드시 setState를 사용하여 변경해야한다.
- state값이 변경되면 useState가 변경을 감지하고, 하위 컴퍼넌트까지 리 렌더링이 발생한다.(하위컴퍼논트가 state를 props로 가지고 있는 경우)
- state값을 그냥 바꾼다면? : 리액트의 render함수를 호출 하지 않아 변경이 일어나도 재 랜더링이 되지 않는다.

## state훅을 통한 Create
``` javascript
newtopics = [...topics]
newtopics.push(value)
Settopics(newtopics)
```


## state훅을 통한 Read
- Settopics에 의해 topics의 내용이 변경될경우 재 랜더링 된다.
``` javascript
{topics} // 해당 state를 Read한다.
```


## state훅을 통한 Update
``` javascript
topics.map((topic) => {
    if (topic.id == 원하는아이디){
        topic.title = 변경하고싶은내용
        topic.body = 변경하고싶은내용
    }
        
})

Settopics(topics)
```

## state훅을 통한 Delete
``` javascript
const newtopics = topics.filter((topic) => {
    topic.id !== 원하는아이디
})

Settopics(newtopics)
```