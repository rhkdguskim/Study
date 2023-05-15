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
