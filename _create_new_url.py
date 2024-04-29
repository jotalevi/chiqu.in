import boto3
import random
import string

dynamodb = boto3.resource('dynamodb')
urls = dynamodb.Table('_urls')

def checkAvailability(short_id):
    response = urls.get_item(Key={'id': short_id})
    return 'Item' not in response

def generateRandomId(length):
    characters = string.ascii_letters + string.digits
    random_id = ''.join(random.choice(characters) for _ in range(length))
    return random_id

def handleRequest(url):
    if not url.startswith('http://') and not url.startswith('https://'):
        url = 'http://' + url
     
    short_id = generateRandomId(6)
    while not checkAvailability(short_id):
        short_id = generateRandomId(6)
    
    urls.put_item(Item={'id': short_id, 'url': url})
    return {'id': short_id, 'url': url}

def lambda_handler(event, context):
    try :
        return handleRequest(event['queryStringParameters']['url'])
    except: 
        return {
            "statusCode": 200,
            "body": """<!doctypehtml><title>CHIQU.IN</title><style>
body,html{min-height:100%;-webkit-appearance:none}body{background-color:#1f1e1e;min-height:100vh;margin:0;padding:0;font-family:"Istok Web",sans-serif;font-weight:400;font-style:normal}.main-div{display:flex;flex-direction:column;flex-wrap:nowrap;align-content:center;justify-content:center;align-items:center;min-height:100vh}.h1{color:#fff;font-size:150px;margin:0;margin-bottom:5px;font-weight:400}.input-div{width:50%;height:75px;background-color:#fff;border-radius:100px;display:flex;flex-direction:row;align-content:center;justify-content:space-between;align-items:center;padding-left:10px;padding-right:10px}.response-div{width:50%;height:75px;background-color:#fff;border-radius:100px;display:flex;flex-direction:row;align-content:center;justify-content:space-between;align-items:center;padding-left:10px;padding-right:10px}.input{height:75px;width:90%;background-color:#fff;border:none;border-radius:100px;margin:0;padding:0;font-size:36px;outline:0}.enter-bt{background-color:#1f1e1e;width:65px;height:65px;border-radius:100px;display:flex;flex-direction:column;flex-wrap:nowrap;align-content:center;justify-content:center;align-items:center;cursor:copy}.nobt{display:none}#typewriter{margin:0;text-align:start;font-size:36px!important}.line-1{position:relative;top:50%;width:24em;margin:0 auto;border-right:2px solid rgba(255,255,255,.75);font-size:180%;text-align:center;white-space:nowrap;overflow:hidden;transform:translateY(-50%)}.anim-typewriter{animation:typewriter 4s steps(44) 1s 1 normal both,blinkTextCursor .5s steps(44) infinite normal}@keyframes typewriter{from{width:0}to{width:24em}}@keyframes blinkTextCursor{from{border-right-color:rgba(255,255,255,.75)}to{border-right-color:transparent}}a{color:#fff;margin-top:25px}
</style><link 
href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200"
rel=stylesheet><style>
.material-symbols-outlined{font-variation-settings:'FILL' 0,'wght' 300,'GRAD' 0,'opsz' 20}
</style><link href=https://fonts.googleapis.com 
rel=preconnect><link href=https://fonts.gstatic.com 
rel=preconnect crossorigin><link 
href="https://fonts.googleapis.com/css2?family=Istok+Web:ital,wght@0,400;0,700;1,400;1,700&display=swap"
rel=stylesheet><script>
window.restext = 'https://chiqu.in/i/'
        window.ell_count = 0;
        window.crrInterval = 0;
        function stepClear() {
            act = document.getElementById('original_url').value
            if (act.length == 0) {
                clearInterval(window.crrInterval);
                window.crrInterval = setInterval(stepEllipsis, 200);
                return
            }
            document.getElementById('original_url').value = act.substring(0, act.length - 1);
        }

        function stepEllipsis() {
            if (window.restext != 'https://chiqu.in/i/') {
                document.getElementById('original_url').value = ''
                clearInterval(window.crrInterval);
                window.crrInterval = setInterval(stepWrite, 100);
                return
            }
            act = document.getElementById('original_url').value
            if (act == '...') {
                window.ell_count += 1;
                act = ''
            } else {
                act = act + '.'
            }
            document.getElementById('original_url').value = act
        }

        function stepWrite() {
            act = document.getElementById('original_url').value
            if (act.length == window.restext.length) {
                clearInterval(window.crrInterval);
                document.getElementById('linkback').classList.remove('nobt')
                return
            }
            document.getElementById('original_url').value = act + window.restext.charAt(act.length);
        }

        function handleGoAction() {
            const myHeaders = new Headers();
            myHeaders.append("Cookie", "_pk_id.1.5367=eb5cdd2448f0b9c3.1698505916.; trafsrc=1bA-OcCJEYdhzhuHrO2DHUYNnsgseNxfProO1bieVqYb7ZgTYVo-my19zg1u-nsOOLIRZzP2gcnEuP6xqW3ZZX5V9vy_MKk; filter[timeFilter]=Q2FrZQ%3D%3D.fg%3D%3D; _pk_id.1.6120=3ab6a4b108f8c2e6.1699751814.; filter[keyFilter]=Q2FrZQ%3D%3D.; filter[genreFilter]=Q2FrZQ%3D%3D.; filter[labelFilter]=Q2FrZQ%3D%3D.; filter[modeFilter]=Q2FrZQ%3D%3D.fw%3D%3D; filter[searchFilter]=Q2FrZQ%3D%3D.; filter[bpmFilter]=Q2FrZQ%3D%3D.; filter[trackTypeFilter]=Q2FrZQ%3D%3D.; snda[data]=Q2FrZQ%3D%3D.NbhxNsAeadg52V6iPwYl1q14JYiVkA1aBOYXQPToHo9ZQE7MmX69ZmlWFSclJPV9o7eLbIj1BZLMpqrd5eA9SyQqzcgev5pX6ChGlln9NlmfhQ%3D%3D; filter[artistFilter]=Q2FrZQ%3D%3D.FbgrapBOPsohpg%3D%3D; _pk_ref.1.5367=%5B%22%22%2C%22%22%2C1712338430%2C%22https%3A%2F%2Fwww.google.com%2F%22%5D; _pk_ses.1.5367=1; snd=opcj3u1emkvhg1nk685i2o7dgi; bruid=1bAlZ6Rxtg8KD97MtnQoYNTKeuz0b_S_tYHibRxtjqE1oSbuTYzWxeu-RTRp9vf5");
            const requestOptions = {
                method: "GET",
                headers: myHeaders,
                redirect: "follow"
            };
            fetch(`https://chiqu.in/?url=${document.getElementById('original_url').value}`, requestOptions)
                .then((response) => response.text())
                .then((result) => {
                    navigator.clipboard.writeText('https://chiqu.in/i/' + JSON.parse(result).id)
                    window.restext = 'https://chiqu.in/i/' + JSON.parse(result).id
                })
                .catch((error) => console.error(error));
            document.getElementById('shrink-div').classList.add('nobt')
            document.getElementById('original_url').placeholder = ''
            window.crrInterval = setInterval(stepClear, 75);
        }</script><div class=main-div><h1 class=h1>
CHIQU.IN</h1><div class=input-div id=input-div><input 
class=input id=original_url name=url 
placeholder="Enter a URL to shorten"><div 
class=enter-bt id=shrink-div onclick=handleGoAction()>
<span class=material-symbols-outlined 
style=color:#fff;font-size:42px>content_copy</span>
</div></div><a class=nobt href=https://chiqu.in 
id=linkback>create another link</a></div>""",
            "headers": {
                'Content-Type': 'text/html',
            }
        }