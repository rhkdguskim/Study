## 요청과 응답 이해하기
- request : 클라이언트 -> 서버
- response : 서버 -> 클라이언트


``` javascript
const http = require('http');

http.createServer((req, res) => {
  // 여기에서 어떻게 응답할지 적는다.
})
```

### server1.js
``` javascript
const http = require('http');

http.createServer((req, res) => {
  res.writeHead(200, {'Content-Type':'text/html; charset-utf-8'});
  res.write('<h1>Hello node</h1>')
  res.end('<p>Hello server</p>')
})
.listen(8080, () => {
  console.log("8080번 포트에서 서버 대기 중입니다!");
})
```

- 포트충돌 : 다른 서비스가 사용하고 있는 포트를 사용할 경우 Error: listen EADDRINUSE ::: 포트 번호 같은 에러가 발생 합니다.
- writeHead : 해더를 기록하는 함수
- write : 본문(body)를 기록 하는 함수
- end : 응답을 종료하는 메서드 만약 인수가 있다면 클라이언트로 보내고 응답을 종료합니다.

### 이벤트 리스너를 등록한 예제
``` javascript

server.on('litening', => () => {
  console.log("8080번 포트에서 서버 대기 중입니다!");
})

server.on('error', => (error) => {
  console.log(error);
})

```

### 한번에 여러개의 서버를 실행할 수 도 있음.

``` javascript

const http = require('http');

const server = http.createServer((req, res) => {
  res.writeHead(200, {'Content-Type':'text/html; charset-utf-8'});
  res.write('<h1>Hello node</h1>')
  res.end('<p>Hello server</p>')
});

server.listen(8080, () => {
  console.log("8080번 포트에서 서버 대기 중입니다!");
})

server.on('litening', => () => {
  console.log("8080번 포트에서 서버 대기 중입니다!");
})

server.on('error', => (error) => {
  console.log(error);
})

http.createServer((req, res) => {
  res.writeHead(200, {'Content-Type':'text/html; charset-utf-8'});
  res.write('<h1>Hello node</h1>')
  res.end('<p>Hello server</p>')
})
.listen(8081, () => {
  console.log("8081번 포트에서 서버 대기 중입니다!");
})

http.createServer((req, res) => {
  res.writeHead(200, {'Content-Type':'text/html; charset-utf-8'});
  res.write('<h1>Hello node</h1>')
  res.end('<p>Hello server</p>')
})
.listen(8082, () => {
  console.log("8082번 포트에서 서버 대기 중입니다!");
})

```

### 미리 작성한 HTML 파일을 fs 모듈을 사용하여 보내기
``` javascript

const http = require('http');
const fs = require('fs').promises;

const server = http.createServer( async (req, res) => {
  try {
    const data = await fs.readFile('./server2.html');
    res.writeHead(200, {'Content-Type':'text/html; charset-utf-8'});
    res.end(data);
  } catch (err) {
    console.log(err);
    res.writeHead(500, {'Content-Type':'text/plain; charset-utf-8'});
    res.end(err.message);
  }

});

server.listen(8080, () => {
  console.log("8080번 포트에서 서버 대기 중입니다!");
})

server.on('litening', => () => {
  console.log("8080번 포트에서 서버 대기 중입니다!");
})

server.on('error', => (error) => {
  console.log(error);
})

```

### HTTP 상태코드
- 2XX : 성공을 알리는 상태코드 , 대표적으로 200(성공), 201(작성됨)이 많이 사용됩니다.
- 3XX : 리다이렉션(다른 페이지로 이동)을 알리는 상태 코드
- 4XX : 요청 오류를 나타냅니다. 403(금지됨), 404(찾을 수 없음)
- 5XX : 서버 오류를 나타냅니다. 요청을 했는데 서버 오류가 발생 했을때 나타내는 오륲

## REST와 라우팅 사용하기
- REST : REpresentation State Fransfer 의 줄임말로, 서버의 자원을 정의하고 자원에 대한 장소를 지정하는 방법을 가리킨다.
- GET : 서버 자원을 가져오가자 할때 사용
- POST : 서버에 자원을 새로 등록하고자 할때 사용
- PUT : 서버 자원을 요청에 들어잇는 지원으로 치환하고자 할때사용
- PATCH : 서버 자원의 일부를 수정하고자 할때
- DELETE : 서버의 자원을 삭제하고자 할때
- OPTION : 통신 옵션을 설명하기 위해 사용한다.

### express웹으로 vics 원격업데이트를 위한 CRUD 구현 및 원격업데이트 요청 코드
``` javascript
const express = require("express");
const fs = require('fs')
const path = require('path')
const {NodeSSH} = require('node-ssh')
const multer = require("multer");

const app = express();

const Vics = new Map();

// 파일 업로드를 위한 multer 설정
const storage = multer.diskStorage({
    destination: "uploads/", // 파일이 저장될 경로
    filename: function (req, file, cb) {
      // 파일 이름 설정
      const uniqueSuffix = Date.now() + "-" + Math.round(Math.random() * 1e9);
      cb(null, file.fieldname + "-" + uniqueSuffix + path.extname(file.originalname));
    },
  });

const upload = multer({ storage });

async function functionVicsUpdate(host, username, password) {
    const ssh = new NodeSSH();
  
    try {
      // SSH 연결 설정
      await ssh.connect({
        host: host, // 접속할 서버 주소
        username: username, // SSH 사용자 이름
        password: password // 서버 접속 비밀번호
      });
  
      
     await ssh.execCommand(`echo ${password} | sudo systemctl stop mivicsd.service`);
     console.log("mivics service stopped !!")

    // 로컬 파일 읽기
    const localFilePath = '/path/to/local/file'; // 로컬 파일 경로
    const localFileContent = fs.readFileSync(localFilePath);

    // 원격 서버로 파일 전송
    const remoteFilePath = '/path/to/remote/file'; // 원격 서버 파일 경로
    await ssh.putFile(localFilePath, remoteFilePath);

    console.log("file transfer end")

    await ssh.execCommand(`echo ${password} | sudo systemctl start mivicsd.service`);
    console.log("mivics service stopped !!")


    } catch (err) {
      console.error('오류:', err);
    } finally {
      // SSH 연결 종료
      ssh.dispose();
    }
}

async function updateVicsList() {
    try{
        for (const [key, value] of Vics) {
            await functionVicsUpdate(value.host, value.username, value.password);
        }
    } catch(err) {
        console.log(err);
    }
}

app.post("/start" , async (req,res) => {
    try{
        await updateVicsList();
        res.json({ message: "작업 완료"});
    } catch(err) {
        console.error("오류:", err);
        res.status(500).json({ error: "작업 실패" });
    }
})

app.post("/upload", upload.single("file"), (req, res) => {
    console.log("파일이 업로드되었습니다.");
    res.send("파일 업로드가 완료되었습니다.");
});

app.get("/vics" , (req,res) => {
    const myArray = Array.from(Vics);
    res.json(myArray);
})

app.post("/vics" , (req,res) => {
    const server =  {
        ip:req.body.ip,
        port:req.body.port,
        username:req.body.username,
        password:req.body.password, 
    }
    Vics.set(req.body.ip, server);
})

app.put("/vics" , (req,res) => {
    Vics.delete(req.body.ip);

    const server =  {
    ip:req.body.ip,
    port:req.body.port,
    username:req.body.username,
    password:req.body.password, 
}
    Vics.set(req.body.ip, server);
    res.json({ message: "작업 완료"});
})

app.delete("/vics" , (req,res) => {
    Vics.delete(req.body.ip);
    res.json({ message: "작업 완료"});
})

app.delete("/vicslist" , (req,res) => {
    Vics.clear();
})

app.listen(8000, () => {
    console.log("서버가 시작되었습니다.");
})
```


### express웹으로 VICS 카메라 CRUD 구현 (미들웨어 구현 포함)
``` javascript
const ffmpeg = require('fluent-ffmpeg');
const ffmpeg_static = require('ffmpeg-static');
var express = require("express");
const expressWs = require("express-ws");
const Datastore = require('nedb');
const router = express.Router();
const cam = require("../classes/camera");
const db = new Datastore({ filename: 'db/CameraDB', autoload: true });
const { spawn } = require('child_process');
const path = require('path');
const fs = require('fs');
const { v4: uuidv4 } = require('uuid');
const { PassThrough } = require('stream');
const { Console } = require('console');
const { Binary } = require('bson');
const {isValidIPandPORT} = require('../classes/common')
require('dotenv').config();
const debug = process.env.DEBUG === 'true';
const axios = require('axios');
const crypto = require('crypto');

ffmpeg.setFfmpegPath(ffmpeg_static);

expressWs(router);
const MycameraList = new Map();

function ReloadData() {
    db.loadDatabase();
}

async function getVicsCamera(ip, port) {
    const username = 'admin';
    const password = 'admin';
  
    try {
      const response = await axios.get(`http://${ip}:${port}/vapi/GetCamList`);
      return response.data;
    } catch (error) {
      if (error.response && error.response.status === 401) {
        const wwwAuthenticateHeader = error.response.headers['www-authenticate'];
        const realmMatch = wwwAuthenticateHeader.match(/realm="([^"]*)"/);
        const nonceMatch = wwwAuthenticateHeader.match(/nonce="([^"]*)"/);
  
        if (realmMatch && nonceMatch) {
          const ha1 = crypto.createHash('md5').update(`${username}:${realmMatch[1]}:${password}`).digest('hex');
          const ha2 = crypto.createHash('md5').update(`GET:/vapi/GetCamList`).digest('hex');
          const nc = '00000001';
          const cnonce = crypto.randomBytes(16).toString('hex');
          const response = crypto.createHash('md5').update(`${ha1}:${nonceMatch[1]}:${nc}:${cnonce}:auth:${ha2}`).digest('hex');
  
          const authResponse = await axios.get(`http://${ip}:${port}/vapi/GetCamList`, {
            headers: {
              Authorization: `Digest username="${username}", realm="${realmMatch[1]}", nonce="${nonceMatch[1]}", uri="/vapi/GetCamList", response="${response}", qop=auth, nc=${nc}, cnonce="${cnonce}"`,
            },
          });
          return authResponse.data;
        }
      }
      console.error(error);
      throw new Error('Failed to get camera list');
    }
  }


db.find({}, (err, cameras) => {
    if(err)
    {
        console.log("error");
    }
    else
    {
        for(idx in cameras)
        {
            const Camera = new cam(cameras[idx].camname, cameras[idx].ip, cameras[idx].port, cameras[idx].username, cameras[idx].password, cameras[idx].id);
            Camera.SetLiveProfile(cameras[idx].liveprofile);
            Camera.SetProtocolType(cameras[idx].protocoltype);
            Camera.start();
            MycameraList.set(cameras[idx].id, Camera);
        }
    }
})

function CheckSrv(req, res, next) {
    if(!isValidIPandPORT(req.body.ip, req.body.port)) {
        res.status(400).json("Invaild Ip And Port");
        return ;
    }
    else{
        next();
    }
  }

  function CheckCam(req, res, next) {
    const id = req.params.id || req.body.id;
    if(MycameraList.get(id) === undefined) {
        res.status(400).json("Invaild ID");
        return ;
    }
    else {
        next();
    }
  }

router.ws('/ws/:id/', (ws, req) => {
    const camid = req.params.id;
    const uuid = uuidv4();
    //console.log("Camera WebSocket Streaming");
    const camera = MycameraList.get(camid);
    // camera.StartMjpegStream(camera.liveprofile);
    camera.StreamList.set(uuid, new PassThrough());
    const stream = camera.StreamList.get(uuid);

    stream.on('data', (data) => {
         ws.send(data, {binary:true});
      });

    ws.on('close', () => {
      camera.StreamList.delete(uuid);
      //console.log('Client disconnected');
    });

    ws.on('message', (data) => {
        console.log("From Client : "+data);
    })
  });

router.post('/', CheckSrv, (req, res) => {
    //console.log(req.body)
        
    const id = uuidv4();
    const camera = {
        id:id,
        camname:req.body.camname,
        ip:req.body.ip,
        port:req.body.port,
        username:req.body.username,
        password:req.body.password,
        liveprofile:req.body.liveprofile || "noprofile",
        protocoltype:req.body.protocoltype || "mp4",
        profile:[],
    };
      
    db.insert(camera, (err, result) => {
        if (err) {
            res.status(500).json(err.message);
        }
        else {
            const Camera = new cam(req.body.camname, req.body.ip, req.body.port , req.body.username, req.body.password, id);
            Camera.SetLiveProfile(req.body.liveprofile || "noprofile");
            Camera.SetProtocolType(req.body.protocoltype);
            Camera.start();
            //Camera.StartCameraStream();
            MycameraList.set(id, Camera);
            res.status(201).json(result);
            ReloadData();
        }
    })
});

router.post('/ptz/:id', (req, res) => {
    
});

router.post('/profile',CheckSrv, (req, res) => {
    const Camera = new cam("fake", req.body.ip, req.body.port , req.session.onvifid, req.session.onvifpwd);
    Camera.connect();

    Camera.Emitter.on("offline", () =>
    {
        res.json({Isonline:false});
    })

    Camera.Emitter.on("profile", (profiles) =>
    {
        res.json({Isonline:true, profiles});
    })

});

router.get('/profile/:id',CheckCam, (req, res) => {
    const Camera = MycameraList.get(req.params.id);
    if(Camera === undefined)
        return;
    //console.log(Camera.profilelist);
    if(Camera.profilelist === undefined)
        return;

    res.json(Camera.profilelist);
});

router.get('/vics/:ip', async (req, res) => {
    const ip = req.params.ip;
    try{
        const data = await getVicsCamera(ip, 9080);
        res.status(201).json(data);
    }
    catch (err) {
        res.status(500).json(err);
    }
    
    
});

router.get('/', (req, res) => {
    db.find({}, (err, cameras) => {
        if (err) {
            res.status(500).json(err.message);
        }
        else{
            res.status(201).json(cameras);
        }
    })
});

router.get('/capture/:id/', CheckCam, (req, res) => {
    camid = req.params.id;
    const camera = MycameraList.get(camid);
    // create a new ffmpeg command
    const command = ffmpeg(camera.rtspurl.get(camera.liveprofile))
      .frames(1) // capture one frame
      //.inputOptions(['-vframes 1'])
      .outputOptions(['-f image2pipe', '-vcodec mjpeg', '-q:v 2'])
      .noAudio()
      .format('image2pipe');
  
    // capture the output from ffmpeg and send in HTTP response
    command.on('error', (err) => {
      console.error(`ffmpeg error: ${err.message}`);
      command.kill();
    })
    .on('end', () => {
       command.kill();
      //console.log('Captured image sent in HTTP response.');
    })
    .pipe(res, { end: true });
    
    //res.set('Content-Type', 'image/jpeg');

  });

router.get('/:id/',CheckCam, (req, res) => {
    const camid = req.params.id;
    const uuid = uuidv4();
    const camera = MycameraList.get(camid);
    
    res.writeHead(200, { // video/mp4
        'Content-Type': 'video/mp4', 
        'Transfer-Encoding': 'chunked',
        'Connection': 'keep-alive',
        });

    const stream = camera.StartMP4Stream(uuid);
    stream.pipe(res);
    
    req.on('close', () => {
        camera.StreamList.delete(uuid);
    });

});

router.delete('/',CheckCam, (req,res) => {
    db.remove({id:req.body.id}, {}, (err, numRemoved) => {
        if(err) {
            res.status(500).json(err);
        }
        else{
            const camera = MycameraList.get(req.body.id);
            camera.stop();
            MycameraList.delete(req.body.id);
            res.status(201).json(numRemoved.toString());
            ReloadData();
        }
    })
});

router.put('/', CheckSrv, (req,res) => {

    const cam = {
        id:req.body.id,
        camname:req.body.camname,
        ip:req.body.ip,
        port:req.body.port,
        username:req.body.username,
        password:req.body.password,
        liveprofile:req.body.liveprofile,
        protocoltype:req.body.protocoltype,
    };

    //console.log('mod');
    const Camera = MycameraList.get(req.body.id);
    Camera.ip = req.body.ip;
    Camera.port = req.body.port;
    Camera.username = req.body.username;
    Camera.password = req.body.password;
    Camera.cameraname = req.body.camname;
    Camera.SetLiveProfile(req.body.liveprofile);
    Camera.SetProtocolType(req.body.protocoltype);
    Camera.stop();
    Camera.connected = false;
    Camera.start();

    db.update({ _id:req.body._id}, { $set: {
        camname : req.body.camname,
        ip : req.body.ip,
        port : req.body.port,
        username : req.body.username,
        password : req.body.password,
        liveprofile : req.body.liveprofile,
        protocoltype : req.body.protocoltype,
    } } , { upsert: true } , (err, numRemoved) => {
        if(err) {
            res.status(500).json(err);
        }
        else{
            res.status(201).json(numRemoved.toString());
            ReloadData();
        }
        
    })
    
});

module.exports = router;
```

### 쿠키와 세션 이해하기
- 로그인을 구현하려면 세션을 알고 있어야한다.
- 쿠키를 서버에 전송한다.

``` javascript
const http = require('http');

http.createSever((req, res) => {
  console.log(req.url, req.headers.cookie);
  res.writeHead(200, {'Set-Cokkie':'mycookie=test'});
  red.end('Hello Cookie');
})
.listen(8083, () => {
  console.log('8083번 포트에서 서버 대기중입니다.')
})
```
- 첫번째 진입시 쿠키에 데이터가 없으므로 undefined 발생
- 두번째 진입시 쿠키게 데이터가 있으므로 로그 찍힘.

``` javascript
const http = require('http');
const fs = require('fs');
const path = require('path');

const parseCokkies = (cookie = '') => {
  cookie
  .split(';')
  .map(v => v.split('='))
  .reduce((acc, [k,v] => {
    acc[k.trim()] = decodeURIComponent(v);
    return acc;
  }), {})
}

http.createServer(async (req, res) => {
  const cookies = parseCookies(req.headers.cookie);

  if(req.url.startsWith('/login')) {
    const url = new URL(req.url, 'http://localhost:8084');
    const name = url.searchParams.get('name');
    const expires = new Date();

    expires.setMinute(expires.getMinutes() + 5);

    req.writeHead(302, {
      Location:'/',
      'Set-Cookie': `name=${endoeURIComponent(name)}; Expires=${expires.toGMTString()}; HttpOnly; Path=/`,
    });
    res.end();
  } else if (cookies.name) {
    res.writeHead(200, {'Content-Type': 'text/plain; charset=utf-8'})
    res.end(`${cookies.name}님 안녕하세요.`)
  } else {
    try {
      const data = await fs.readFile(path.join(__dirname, 'cookie2.html'));
      res.writeHead(200, {'Content-Type':'text/html; charset=utf-8'});
      res.end(data);
    } catch (err) {
      res.writeHead(500, {'Content-Type':'text/plain; charset=utf-8'})
      res.send(err.message);
    }
  }
})
.listen(8084, () => {
  console.log('8084번 포트에서 서버 대기중입니다.')
})

```
- /login과 /로 분리함
- parseCookie 함수는 쿠키 문자열을 쉽게 사용하기 위해 자바스크립트 객체 형식으로 바꾸는 함수
- 민감한 개인정보를 쿠키에 넣어두는 것은 적절하지 못합니다.

``` javascript
const http = require('http');
const fs = require('fs');
const path = require('path');

const parseCokkies = (cookie = '') => {
  cookie
  .split(';')
  .map(v => v.split('='))
  .reduce((acc, [k,v] => {
    acc[k.trim()] = decodeURIComponent(v);
    return acc;
  }), {})
}

http.createServer(async (req, res) => {
  const cookies = parseCookies(req.headers.cookie);

  if(req.url.startsWith('/login')) {
    const url = new URL(req.url, 'http://localhost:8084');
    const name = url.searchParams.get('name');
    const expires = new Date();
    expires.setMinute(expires.getMinutes() + 5);
    const uniqueInt = Date.now();
    session[uniqueInt] = {
      name,
      expires,
    }

    req.writeHead(302, {
      Location:'/',
      'Set-Cookie': `session=${uniqueInt}; Expires=${expires.toGMTString()}; HttpOnly; Path=/`,
    });
    res.end();
  } else if (cookies.session && session[cookies.session].expires > new Date()) {
    res.writeHead(200, {'Content-Type': 'text/plain; charset=utf-8'})
    res.end(`${session[cookies.session].name}님 안녕하세요.`)
  } else {
    try {
      const data = await fs.readFile(path.join(__dirname, 'cookie2.html'));
      res.writeHead(200, {'Content-Type':'text/html; charset=utf-8'});
      res.end(data);
    } catch (err) {
      res.writeHead(500, {'Content-Type':'text/plain; charset=utf-8'})
      res.send(err.message);
    }
  }
})
.listen(8084, () => {
  console.log('8084번 포트에서 서버 대기중입니다.')
})

```
- 서버에 사용자 정보를 저장하고 클라이언트와 세션 아이디로만 소통 합니다. 세션 아이디는 꼭 쿠키를 사용하여 주고 받지 않아도 됩니다.

### https와 http2
- https 모듈은 웹 서버에 SSL 암호화를 추가합니다. GET이나 POST 요청이 오가는 데이터를 암호화해서 중간에 다른사람이 요청을 가로채더라도 내용을 확인 할 수 없게 합니다. 요즘은 로그인이나 결제가 필요한 창에서 https 적용이 필수가 되는 추세입니다.
- https모듈을 사용해야함. 하지만 https는 아무나 사용불가, 인증서는 인증기관에서 발급하거나 무료로 받을 수 있다.

``` javascript
const https = requre('https');
const fs = require('fs');

https.createServer({
  cert: fs.readFileSync('도메인 인증서 경로'),
  key: fs.readFileSync('도메인 비밀 키 경로'),
  ca : [
    fs.readFileSync('상위 인증서 경로'),
    fs.readFileSync('상위 인증서 경로'),
  ],
}, (req, res) => {
  res.writeHead(200, {'Content-Type':'text/html; charset=utf-8'});
  res.write('<h1>Hello Node!</h1>')
  res.write('<p>Hello Server!</p>')
})
.listen(443, () => {
  console.log('443번 포트에서 서버 대기 중 입니다');
})
```

``` javascript
const http2 = requre('http2');
const fs = require('fs');

http2.createSecureServer({
  cert: fs.readFileSync('도메인 인증서 경로'),
  key: fs.readFileSync('도메인 비밀 키 경로'),
  ca : [
    fs.readFileSync('상위 인증서 경로'),
    fs.readFileSync('상위 인증서 경로'),
  ],
}, (req, res) => {
  res.writeHead(200, {'Content-Type':'text/html; charset=utf-8'});
  res.write('<h1>Hello Node!</h1>')
  res.write('<p>Hello Server!</p>')
})
.listen(443, () => {
  console.log('443번 포트에서 서버 대기 중 입니다');
})
```
- http 모듈과 거의 유사함. https 모듈을 http2로, createServer 메서드를 createSecure Server 메서드로 바꾸면 됨.

### cluster
- 클러스터 모듈은 기본적으로 싱글 프로세스로 동작하는 노드가 CPU 코어를 모두 사용 할 수 있게 해주는 모듈입니다.
- 메모리를 공유하지 못하는 장점 -> 레디스 등의 서버를 도입하여 해결 할 수 있다.

``` javascript
const cluster = require('cluster');
const http = require('http');
const numCPUs = require('os').cpus().length;

if(cluster.isMaster) {
  console.log(`마스터 프로세스 아이디 : ${process.pid}`);
  for(let i = 0; i < numCPUs; i++) {
    cluster.fork();
  }

  cluster.on('exit', (worker, code, signal) => {
    console.log(`${worker.process.pid} 번이 종료되었습니다.`)
    console.log('code',code,'signal',signal);
  })
} else {
  http.createSever((req, res) => {
  res.writeHead(200, {'Content-Type':'text/html; charset=utf-8'});
  res.write('<h1>Hello Node!</h1>')
  res.end('<p>Hello Cluster!!</p>')
}).listen(8086)

  console.log(`${worker.process.pid} 번 워커 실행`)
}
```
- worker_threads 예제와 모양이 비슷함, 다만 스레드가 있는게 아니라 프로세스입니다.
- 클러스터 모듈로 클러스터링을 구현 할 수 있지만, 실무에서는 pm2등의 모듈로 cluster기능을 사용하곤 합니다.