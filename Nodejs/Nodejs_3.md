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


## 노드 내장 모듈 사용하기
### os
- 자바스크립트는 운영체제 정보를 가져 올 수 없지만 노드는 정보를 가져올 수 있습니다.
- require('os') : 내장모듈

```javascript
const os = require('os');

const getOSInfo = () => {
  console.log(os.arch());
  console.log(os.platform());
  console.log(os.type());
  console.log(os.uptime());
  console.log(os.hostname());
  console.log(os.release());
  console.log(os.homedir());
  console.log(os.tmpdir());

  console.log(os.cpus());
  console.log(os.cpus().length);

  console.log(os.freemem());
  console.log(os.totalmem());
}

```


### path
- 운영체제 별로 경로 구분자가 다르기때문에 필요하다.
- 윈도타입 : \
- POSIX 타입 : /

```javascript
const path = require('path');

console.log(path.sep);
consloe.log(path.delimiter)

---------------------------------------
consloe.log(path.dirname())
consloe.log(path.extname())
consloe.log(path.basebane())

---------------------------------------
path.parse();
path.format();
path.normalize();

---------------------------------------
path.isAbsolute(c:\\); // true
path.isAbsolute(./home);  // false

--------------------------------------------
path.relative();
path.join();
path.resolve();

```
- join과 resolve의 차이 resolve는 절대경로로 인식하여 앞의 경로를 무시하고 join은 상대경로로 처리 한다.
- 자바스크립트에서 \는 특수문자임으로 \\로 표시해야합니다.
- path모듈은 위와같은 발생하는 에러에 대해서 알아서 처리합니다. 따라서 특히 윈도에서 path 모듈이 꼭 필요합니다.


### URL
- 인터넷 주소를 쉽게 조적하도록 도와주는 모듈입니다.
- WHATWG방식 URL
- 노드에서 사용하던 방식의 URL
- 생성자에 주소를 넣어 객체로 만들면 부분별로 정리됨 -> WHATWG URL 방식
- URLSearchParams : 이 객체는 search 부분을 조작하는 다양한 메서드를 지원
- getAll(키), get(키), has(키) ...

### DNS
- DNS를 다룰때 사용하는 모듈입니다. 주로 도메인을 통해 IP나 기타 DNS정보를 얻고자 할때 사용합니다.
- IP주소는 dns.lookup이나 dns.resolve로 얻을 수 있씁니다.

### crypto
- 다양한 방식의 암호화를 도와주는 모듈입니다. 몇 가지 메서드는 익혀두면 실제 서비스에도 적용 할 수 있어 유용합니다.
- 단방향 암호화 : 비밀번호는 보통 단방향 암호화를 사용하여 암호화 한다. (복호화 불가능) -> 해시함수라고도 함.
- 암호화를 통하여 유저 db에 저장하고 불러오는 기능을 구현
```javascript
 router.post("/", (req, res) => {
    // 비밀번호 해싱하기
    console.log(req.body.username);
    db.find({key : req.body.username}, (err, user) => {
        console.log(Object.keys(user).length);
        if(!Object.keys(user).length)
        {
            const hash = crypto.createHash('md5').update(req.body.password).digest('hex');
            const user = {
            username : req.body.username,
            password : hash,
            onvifid  : req.body.onvifid,
            onvifpwd : req.body.onvifpwd,
            key : req.body.username
            }
        
            db.insert(user, (err, result) => {
            if (err) {
                res.status(500).send(err.message);
            }
            else {
                req.session.islogined = true;
                res.status(201).send(result);
            }
            });
        }
        else
        {
            res.status(201).send("User is already exsist");
        }
    });
    
 })
 
 
 
 router.post("/login", (req, res) => {
    db.find({key : req.body.username}, (err, user) => {
        if(err)
        {
            console.log("there is no users!!");
        }
        else
        {
            if(Object.keys(user).length)
            {
                const hash = crypto.createHash('md5').update(req.body.password).digest('hex');
                if(user[0].password === hash) {
                   req.session.islogined = true;
                   req.session.username = req.body.username;
                   req.session.onvifid = user[0].onvifid;
                   req.session.onvifpwd = user[0].onvifpwd;
                   res.send({Logined:true});
               }
               else {
                res.send({Logined:false, err:"password"});
               }
            }
            else{
                res.send({Logined:false, err:"nouser"});
            }
            
        }
        
    })
 })

```
- 양방향 암호화 : 암호화된 문자열을 복호화 할 수 있으며 키(열쇠)라는 것이 사용됩니다. 암호활때 사용했던키와 복호화할때 사용할 키가 같아야합니다.

### util
- util 이라는 이름처럼 각종 편의 기능을 모와둔 모듈이다.
- util.deprecate: 함수가 deprecated처리 되었음을 알려준다. ,util.promisify: 콜백 패턴을 프로미스 패턴으로 바꿔준다.

### worker_threads
- 노드에서 멀티 스레드 방식으로 작업하는 방법

```javascript
const {
    Worker, isMainThread, parentPort, }
    = require('worker_threads');
    
    if(isMainThread) { // 부모 스레드일때
    const worker = new Worker(__filename);
    worker.on('message', message => console.log('form worker', message));
    worker.on('exit', () => console.log('worker exit'));
    worker.poseMessage('ping');
    }
    else // 워커일때
    {
        parentPort.on('message', (value) => {
            console.log('from parent', value);
            parentPort.poseMessage('pong');
            parentPort.close();
        }
    }
```
- isMainThread를 통해 현재 코드가 메인 스레드에서 실행되는지 아니면 우리가 생성한 워커스레드에서 실행되는지 구분됩니다.
- 메인스레드에서는 new Worker를 통해 현재파일 워커 스레드에서 실행시키고 있습니다.
- else 부분은 워크스레드에서만 실행됩니다.

```javascript
const {
    Worker, isMainThread, parentPort, }
    = require('worker_threads');
    
 if(isMainThread) { // 부모 스레드일때
    const threads = new Set();
    threads.add(new Worker(__filename, {
        workerData: { start:1 }
    }));
    threads.add(new Worker(__filename, {
        workerData: { start:2 }
    }));
    }
    for (let worker of threads) {
        worker.on('message', message => console.log('form worker', message ));
        worker.on('exit', () => {
            threads.delete(worker);
            if(threads.size === 0 ) {
                console.log('job done');
            }
        });
    }
    else // 워커일때
    {
        const data = workerdata;
        parentPort.postMessage(data.start + 100);
    }

```
- new Worker를 호출할 때 두 번째 인수의 workerData 속성으로 원하는 데이터를 보낼 수 있씁니다.
- 두개의 워커가 돌아가고 있으며 각 부모로부터 숫자를 받아서 100을 더해 돌려줍니다. 

### child_process
- 노드에서 다른 프로그램을 실행하고 싶거나 명령어를 수행하고 싶을때 사용하는 모듈 입니다.
- 이 모듈을 통해서 결과값을 받을 수 있습니다.

```javascript
const exec = require('child_process').exec;

const process = exec('dir');

process.stdout.on('data', function(data) {
    console.log(data.toString());
});

process.stderr.on('data', function(data) {
    console.error(data.toString());
});

```

- exec의 첫번째 인수로 명령어를 넣습니다.
- 결과는 stdout(표준출력)과 stderr(표준에러)에 붙혀둔 data 이벤트 리스너에 버퍼 형태로 전달됩니다. 성공적인 결과는 표준출력, 실패한 경과는 표준에러에서 표시됩니다.
- exec와 spawn의 차이 : exec은 셸을 실행해서 명령어를 수행하고, spawn은 새로운 프로세스를 띄우면서 명령어를 실행합니다.

```javascript
StartMP4Stream(profile) { // MP4 Stream 생성

      const args =  debug ? [
        '-i',
        `BigBuckBunny.mp4`,
        '-vcodec',
        'copy',
        '-f',
        'mp4',
        `-preset`, `ultrafast`,
        `-tune`, `zerolatency`,
        '-movflags',
        'frag_keyframe+empty_moov+default_base_moof',
        'pipe:1',
      ] : [
        '-rtsp_transport','udp',
        '-rtsp_flags', 'listen',
        '-i',
        `${this.rtspurl.get(profile)}`,
        '-vcodec',
        'copy',
        '-f',
        'mp4',
        `-preset`, `ultrafast`,
        `-tune`, `zerolatency`,
        '-movflags',
        'frag_keyframe+empty_moov+default_base_moof',
        'pipe:1',
      ]

      const ChildProcess = spawn(ffmpeg_static, args);

      this.StreamProcess.set(profile, ChildProcess);

      ChildProcess.stderr.on('data', (data) => {
        if(debug)
          console.log(data.toString());
      });

      ChildProcess.stdout.on('start', () => {
        if(debug)
          console.log("Stream Stared start");
      });

      ChildProcess.stdout.on('end', () => {
        if(debug)
          console.log("Stream End");
      });

      return ChildProcess;
    }

    StartHLSStream(profile) { // HLS Stream 생성
      if(this.StreamProcess.has(profile))
      {
        console.log("already Exsist");
        return this.StreamProcess.get(profile);
      }  

      const dir = `./hls/${this.id}`;

      if (!fs.existsSync(dir)) {
        fs.mkdirSync(dir, { recursive: true });
      }

      const args = debug ?  [
        '-rtsp_transport','udp',
        '-rtsp_flags', 'listen',
        '-i',
        `BigBuckBunny.mp4`, // ${this.rtspurl.get(profile)}
        '-vcodec',
        'copy',
        '-f', 'hls', // hls 스트리밍
        '-hls_time', '2', // ts 파일 크기
        `-hls_list_size`,'10', // ts파일 개수
        `-preset`, `ultrafast`,
        `-tune`, `zerolatency`,
         '-hls_init_time', '1',
        `-hls_segment_filename`, `hls/${this.id}/ts_%03d.ts`, // ts 파일 포맷 설정
        `-hls_flags` , `delete_segments+append_list`, // ts파일 삭제
         `hls/${this.id}/play.m3u8`, // output파일 지정
      ] :
      [
        '-rtsp_transport','udp',
        '-rtsp_flags', 'listen',
        '-i',
        `${this.rtspurl.get(profile)}`, // ${this.rtspurl.get(profile)}
        '-vcodec',
        'copy',
        '-f', 'hls', // hls 스트리밍
        '-hls_time', '2', // ts 파일 크기
        `-hls_list_size`,'10', // ts파일 개수
        `-preset`, `ultrafast`,
        `-tune`, `zerolatency`,
         '-hls_init_time', '1',
        `-hls_segment_filename`, `hls/${this.id}/ts_%03d.ts`, // ts 파일 포맷 설정
        `-hls_flags` , `delete_segments+append_list`, // ts파일 삭제
         `hls/${this.id}/play.m3u8`, // output파일 지정
      ]
      
      const ChildProcess = spawn(ffmpeg_static, args);

      this.StreamProcess.set(profile, ChildProcess);

      ChildProcess.stderr.on('data', (data) => {
        if(debug)
          console.log(data.toString());
      });

      ChildProcess.stdout.on('start', () => {
        if(debug)
          console.log("Stream Stared start");
      });

      ChildProcess.stdout.on('end', () => {
        console.log("end");
        //this.KillStreamProcess(profile);
      });

      return ChildProcess;
    }

    StartMjpegStream(profile)
    {
      const args = [
        '-i',
        `BigBuckBunny.mp4`, //`${camera.rtspurl.get(camera.liveprofile)}` // this.rtspurl.get(profile)
         '-vcodec',
         'copy',
         '-r', '30',
        '-f',
        'mp4',
        `-preset`, `ultrafast`,
        `-tune`, `zerolatency`,
        '-movflags', 'frag_keyframe+empty_moov',
        'pipe:1',
      ];
      
      const ChildProcess = spawn(ffmpeg_static, args);

      this.StreamProcess.set(profile, ChildProcess);

      ChildProcess.stdout.on('start', () => {
        console.log("Stream Stared start");
      });

      ChildProcess.stdout.on('end', () => {
        console.log("end");
      });
    }

```

### 기타 모듈들
- async_hook : 비동기 코드의 흐름을 추척 할 수 있는 실험적인 모듈 입니다.
- dgram : UDP와 관련된 작업을 할 때 사용합니다.
- net : HTTP 보다 로우 레벨인 TCP나 IPC 통신을 사용할때 사용합니다.
- pref_hooks : 성능 측정을 할때 사용합니다.
- querystring : URLSearchParams 가 나오기 이전에 쿼리스트링을 다루기 위해 사용햇던 모듈 입니다.
- string_decoder : 버퍼 데이터를 문자열로 바꾸는데 사용합니다.
- tls : TLS와 SSL에 관련된 작업을 사용할때 사용합니다.
- v8 : V8엔진에 직접 접근할때 사용합니다.
- vm : 가상머신에 직접 접근할때 사용합니다.
- wasi : 웹어셈블리를 실행할때 사용하는 실험적인 모듈입니다.

## 파일 시스템 접근하기.
```javascript
const fs = require('fs');

fs.readfile('./readme.txt', (err, data) => {
    if(err) {
        throw err;
    }
    console.log(data);
    console.log(data.toString());
}

```

### 동기 메서드와 비동기 메서드
- 동기와 비동기 : 백그라운드 작업 완료 확이 여부
- 블로킹과 논블로킹 : 함수가 바로 return 되는지 여부

### 버퍼와 스트림 이해하기
#### 버퍼
- 파일을 읽거나 쓰는 방식에는 두가지 방식이 있습니다. 버퍼를 이용하거나 스트림을 이용하는 방식 ( 버퍼링과 스트리밍 )
- form(문자열) : 문자열을 버퍼로 바꿀 수 있습니다.
- toString(버퍼) : 버퍼를 다시 문자열로 바꿀 수 있습니다. 이때 base64나 hex를 인수로 넣으면 해당 인코딩으로도 변환 가능합니다.
- concat(배열) : 배열 안에 든 버퍼들을 하나로 합칩니다.
- accoc(바이트) : 빈 버퍼를 생성합니다.

### 스트림
- 버퍼의 크기를 작게 만들고 여러번에 걸쳐 나눠 보내는 방식

#### ReadStream
```javascript
const fs = require('fs');

const readStream = fs.createReadStream('./readme3.txt', { highWaterMark:16 } );
const data = [];

readStream.on('data', (chunk) => {
    data.push(chunk);
    console.log('data :', chunk, chunk.length);
});

readStream.on('end', () => {
    console.log('end :', Buffer.concat(data).toString());
});

readStream.on('error', (err) => {
    console.log('error : ' , err);
});

```

#### WriteStream
```javascript
const fs = require('fs');

const writeStream = fs.createWriteStream('./writeme2.txt');
writeStream.on('finish', () => {
    console.log("파일 쓰기 완료");
});

writeStream.write('이 글을 씁니다. \n');
writeStream.write('한 번 더 씁니다. ');
writeStream.end();


```

#### ReadStream과 WriteStream의 파이브
```javascript
const fs = require('fs');

const readStream = fs.createReadStream('readme4.txt');
const writeStream = fs.createWriteStream('writeme3.txt');
readStream.pipe(writeStream);

```

#### fs기타 메서드
- fs.access : 폴더나 파일에 접근 할 수 있는지 체크합니다.
- fs.mkdir : 폴더를 만드는 메서드입니다. 이미 폴더가 있다면 에러가 발생합니다.
- fs.open : 파일의 아이디를 가져오는 메서드입니다.
- fs.rename : 파일 이름을 바꾸는 메서드입니다.
- fs.readdir : 폴더안의 내용물을 확인 할 수 있씁니다.
- fs.unlink : 파일을 지울 수 있습니다.
- fs.redir : 폴더를 지울 수 있습니다.
- fs.copyFile : 파일복사
- fs.watch : 파일/폴더 변경사항을 감시 할 수 있는 메서드

## 스레드 풀
- 그동안 fs메서드를 여러번 실행해도 백그라운드에서 동시에 처리되는데 바로 스레드 풀이 있기 때문입니다.
- fs 외에도 내부적으로 스레드 풀을 사용하는 모듈로는 crypto, zilb, dns, lookup 등이 있음.
- 기본적으로 세레드 풀의 개수가 4개 이다. 컴퓨터코어 개수가 4개보다 다르다면 그렇지않을 수 있다.
- UV_THREADPOOL_SIZE=스레드 풀 개수
- 컴퓨터 코어의 개수와 같거나 그보다 많이 둬야 뚜렷한 효과가 발생한다.

## 이벤트 이해하기
- 스트림을 배울때 on('data', 콜백) ... 있었는데 이벤트가 발생할때 콜백함수를 호출하도록 이벤트를 등록한것이다.
- 

- 카메라 Online, Offline, profiles , rtsp 주소 이벤트 콜백 구현
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
      
      this.StreamProcess = new Map();

      this.rtspurl = new Map();
      this.profilelist = [];
      this.Emitter = new EventEmitter();
    }
    
    Callbackfunc(err)
    {
        if (err) {
            this.connected = false;
            this.Emitter.emit('offline', (err));
            //console.log('Connection Failed for ' + this.ip + ' Port: ' + this.port + ' Username: ' + this.username + ' Password: ' + this.password);
            return;
        }
        this.connected = true;
        this.Emitter.emit('online');
        this.getCapabilities((err, capabilities) => {
          if (err) {
            console.error('Error getting media capabilities:', err);
            return;
          }
          //console.log(capabilities);
        });
      
         //console.log("[Camera Connected] "+"IP: " + this.ip + ' Port: ' + this.port);
         this.getProfiles(function(err, profiles) {
            //console.log(profiles[0].$.token);
            if (err) {
              console.log('Error: ' + err.message);
            } else {
            for(let i=0; i<profiles.length; i++)
            {
              const profilename = profiles[i].$.token;
              //console.log(profilename);
              this.getStreamUri({
                protocol: 'RTSP',
                profileToken: profilename
              }, function(err, stream) {
                if (err) {
                  console.log('Error: ' + err.message);
                } else {
                  stream.uri = stream.uri.slice(7);
                  //console.log(`rtsp://${this.username}:${this.password}@`+ stream.uri);
                  this.rtspurl.set(profilename, `rtsp://${this.username}:${this.password}@`+ stream.uri);
                  if(debug)
                    console.log("RtspUrl Map : ", this.rtspurl);
                }
              });
            }
            //console.log(profiles);
            //const keysToKeep = [$.token]; // 제외할 키 목록

            profiles.map((obj) => {
              //console.log(obj.$.token)
              this.profilelist.push({name : obj.$.token});
              }
              );
            //console.log(this.profilelist, this.ip);
            //this.profilelist = profiles;
            this.Emitter.emit('profile', (this.profilelist));
            }
          });
    }

```

### 예외 처리하기
- 노드에서는 예외처리가 정말 중요합니다.
- 멀티 스레드 프로그램에서 스레드 하나가 멈추면 다른스레드가 대신합니다. 하지만 메인 스레드는 하나뿐임으로 소중히 보호해야한다.
- 에러로그가 기록되더라도 작업은 계속 진행 될 수 있게 해야한다.
- 노드 16 버전부터는 프로미스의 에러는 반드시 catch 해야합니다. catch 하지 않으면 에러와 함께 노드 프로세스가 종료됩니다.
- uncaughtException 이벤트 리스너로 모든 에러를 처리할 수 있다(?)

#### 자주 발생하는 에러들
- node : command not found 대부분이 환경변수 문제
- ReferenceError : 모듈 is not defined : 해당 모듈을 require 했지만 설치 하지 않았습니다.
- error : Can't set headers after they are sent : 요청에 대한 응답을 보낼때 응답을 두번이상 보냈습니다. 요청에 대한 응답은 한번만 보내야합니다.
- FATAL ERROR : CALL_AND_RETRY_LAST Allocation failed - JavaScripte heap out of memory : 코드를 잘 못 구현했을 가능성 이 있음.
- UnhandledPromiseRejectionWaring : 프로미스 사용시 catch 메서드를 붙히지 않으면 발생하는 에러
- EADDRINUSE 포트 번호 : 해당 포트 번호에 이미 다른 프로세스가 연결되어있습니다.


