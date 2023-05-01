## const, let
- var 변수 선언 형식은 const, let이 대체한다.
- 함수 스코프 : 함수 안에 { }
- 블록 스코프 : if , while , for, function 등에서 볼 수 있는 {  }
- const : 한번 선언만 가능, 함수 스코프
- let : 블록 스코프, 변경 가능

## 템플릿 문자열
- 백틱(`): 문자열 안에 변수를 넣을 수 있음.
- ${변수} 사용으로 백틱 안에 넣을 수 있음.

## 객체 리터럴
- 객체의 메서드에 함수를 연결 할때 콜론(:)을 붙이지 않아도 된다.
- 속성명과 변수명이 동일한 경우 생략가능 {name : name, age: age} -> { name, age }

## 화살표 함수
- 화살표 함수라는 새로운 함수가 추가됨
- 내부에 return 문 밖에 없는 경우 생략가능
- 매개변수가 하나이면 괄호를 묶지 않아도 됨

### 기존
```javascript
function test(req, res) {
  return res.send(req.body);
}
```
### 이후
```javascript
const test = (req,res) => { res.send(req.body) }
```
### forEach 함수
- 배열오소들을 각각에 대하여 지정된 콜백 함수를 실행시킵니다.
```javascript
const array = [1, 2, 3, 4, 5];

array.forEach((element) => {
  console.log(element);
});

```

## 구조 분해 할당
- 모듈시스템에서 구조분해할당을 많이 사용한다.
```javascript
const { getCandy, status: { count } } = candyMachine;

const array = ['nodejs', {}, 10, true];
const [ node, obj, , boo ] = array;
```

## 클래스
- 클래스 문법도 추가됨
- 다른 언어처럼 클래스 기반으로 동작하는 것이 아닌 프로토타입 기반 동작

### 프로토타입
- 객체 지향 프로그래밍에서 상속을 구현하는 방식중 하나.
- 자바스크립트 모든 객체는 프로토타입이라는 내부 객체를 가르킨다.
- 프로토타입 링크는 부모객체를 가르킨다. ( 프로토타입 체인 )
- 프로토 타입 기반 상속 ( 프로토타입으로 상속 관계를 구현 가능 )

### 상속 예제
```javascript
class Camera extends onvifCam {
    constructor(camname, ip, port, username, password , id) {
    super({hostname : ip, username, password, port,autoconnect:false, timeout:10000})
      this.ip = ip;
      this.port = port;
      this.username = username;
      this.password = password;
      this.cameraname = camname;
      this.id = id;
      
      this.fluentffmpeg = new Map();
      this.ffmpegStreams = new Map();
      this.rtspurl = new Map();

      this.Emitter = new EventEmitter();
    }
    
       connect()
    {
        if(!this.connected)
            super.connect(this.Callbackfunc);
    }
```

## 프로미스
- 자바스크립트와 노드는 비동기를 사용
- 이벤트 리스너에 콜백함수 사용
- ES2015부터는 API들이 콜백 대신 프로미스 기반으로 재구성
- resolve, reject, then, catch, finanlly
- resolve 시 then로 실행
- reject시 catch로 실행
- finally는 항상 실행
- all로 프로미스 병합
- allSettled로 프로미스 상태 확인

### all, allsettled 예제
```javascript
const promise1 = Promise.resolve("성공");
const promise2 = Promise.resolve("성공");
Promise.all([promise1, promise2])
.then((result)) => {
  console.log(result); // ['성공1', '성공2']
}
.catch((err) => {
  console.log(err);
});
```
## async, await
- ES2017에서 추가됨
- 프로미스 문을 더 깔끔하게 줄일 수 있음.
- try/catch 문으로 로직을 감쌀 수 있음.
- await of 를 통하여 기존 프로미스 배열을 순회 가능

### fecth 함수 활용
```javascript
  async function CheckProfile (event) {
    const camera = {
     ip:ip.current.value, port:port.current.value
  }

  const response = await fetch("/camera/profile", {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(camera)
  })
  const json = await response.json();
  console.log(json);
  if(json.Isonline)
  {
    if(json.profiles.length)
    {
      Setcamprofiles(json.profiles);
    }
  }
};
```

## Map/Set
- Map : key, value 형태의 자료구조
- Set : 순서보장, 속성의 수를 쉽게 알 수 있음, 중복 방지 가능
```javascript
   this.fluentffmpeg = new Map();
   this.ffmpegStreams = new Map();
   this.rtspurl = new Map();
   
   this.rtspurl.set(profiles[i].name, `rtsp://${this.username}:${this.password}@`+ stream.uri);
   
         const args = [
        '-i',
        `${this.rtspurl.get(profile)}`, //`${camera.rtspurl.get(camera.liveprofile)}`
        '-vcodec',
        'copy',
        '-f',
        'mp4',
        `-preset`, `ultrafast`,
        `-tune`, `zerolatency`,
        '-movflags',
        'frag_keyframe+empty_moov+default_base_moof',
        'pipe:1',
      ];
   
```

## 널 병합/옵셔널 체이닝
### 널 병합 연산자
- || : falsy 값이면 뒤로 넘어감
- ?? null과 undefined일때만 뒤로 넘어감
### 옵셔널 체이닝 연산자
- null이나 undefined의 속성을 조회하는 경우 에러가 발생하는것을 막음.
```javascript
const c = null;
c?.d // 문제없음
c?.f() // 문제 없음
c?.[0] // 문제없음
```

## 프런트엔드 자바스크립트
- AJAX는 비동기적 웹 서비스를 개발 할때 사용하는 기법
- 요즘은 JSON을 많이 사용함.
- AJAX 요청은 jQuery나 axios같은 라이브러리를 이용하여 보냄.

### Get 빙식
```javascript
  async function fetchData() {
    const response = await fetch('/camera/');
    const json = await response.json();
    //setData(json);
    for(let i=0; i<json.length; i++)
    {
      const response2 = await fetch(`/camera/profile/${json[i].id}`);
      const json2 = await response2.json();
      console.log(json2);
      json[i].profile=json2;
    }
    setData(json);
    //const response2 = await fetch('/camera/profile/');
    //const json2 = await response.json();
    console.log(data);
    };
```

### POST 방식
```javascript
  const response = await fetch("/camera/profile", {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(camera)
  })
  const json = await response.json();
  console.log(json);
  if(json.Isonline)
  {
    if(json.profiles.length)
    {
      Setcamprofiles(json.profiles);
    }
  }
};

  const handleSubmit = (event) => {
    event.preventDefault();
    
    const camera = {
        camname:camname.current.value, 
        ip:ip.current.value, 
        port:port.current.value, 
        username:id.current.value, 
        password:pwd.current.value,
        liveprofile:profile,
        protocoltype:protocol,
    }
    console.log(camera);

    fetch("/camera/", {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(camera)
      })
      .then(response => response.json())
      .then(data => console.log(data))
      .catch(error => console.error(error));
  };
```

### DELETE 방식
```javascript
async function handleDelClick(params) {
  console.log(params);
  const response = await fetch("/camera/", {
    method: 'DELETE',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({id:params.id})
  })
  const json = await response.json();
}
```

### PUT 방식
```javascript
async function handleProfileComboChange (event) {
  selectedRow.liveprofile = event.target.value;
  console.log(selectedRow);
  const response = await fetch("/camera/", {
    method: 'PUT',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(selectedRow)
  })
  
  fetchData();
```

### FormData 
- HTML form 태그의 데이터를 동적으로 제어 할 수 있는 기능이다.
- 서버에 요청할 데이터를 정리하기에 용이 한거 같다.

### encodeURIComponent, decodeURIComponet
- URI 에 한글이 들어가는 이슈를 해결합니다.

### 데이터 속성과 dataset
- data-로 시작하는 것들을 넣습니다.
- 데이터속성은 자바스크립트에서 쉽게 접근가능하다.
