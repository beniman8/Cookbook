html_content = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Programming Jeopardy Chat Edition</title>

<script src="https://unpkg.com/tmi.js@1.8.5/dist/tmi.min.js"></script>

<style>
body{margin:0;font-family:Arial;background:transparent;color:white;}
.score{position:absolute;top:30px;left:40px;font-size:30px;background:#001a66;border:3px solid gold;padding:10px 25px;border-radius:10px;}
.player{position:absolute;top:30px;right:40px;font-size:28px;background:#001a66;border:3px solid gold;padding:10px 25px;border-radius:10px;}
.board{display:grid;grid-template-columns:repeat(5,1fr);gap:10px;width:85%;margin:120px auto;}
.category{background:#0026ff;text-align:center;padding:15px;font-weight:bold;border:3px solid gold;font-size:22px;}
.tile{background:#003cff;border:3px solid gold;text-align:center;padding:30px;font-size:32px;cursor:pointer;}
.tile:hover{background:gold;color:black;}
.used{visibility:hidden;}
.questionScreen{position:absolute;top:0;left:0;width:100%;height:100%;background:#000b4d;display:none;flex-direction:column;justify-content:center;align-items:center;text-align:center;padding:40px;}
.timer{font-size:70px;margin-bottom:20px;border:3px solid gold;padding:10px 40px;border-radius:10px;background:#001a66;}
.question{font-size:40px;margin-bottom:20px;max-width:1000px;}
.answers{font-size:30px;margin-top:20px;line-height:50px;}
.result{font-size:36px;color:gold;margin-top:30px;}
</style>
</head>

<body>

<div class="score" id="score">Score: 0</div>
<div class="player">Rayman</div>

<div class="board" id="board"></div>

<div class="questionScreen" id="questionScreen">
<div class="timer" id="timer">30</div>
<div class="question" id="questionText"></div>
<div class="answers" id="answersText"></div>
<div class="result" id="resultText"></div>
</div>

<script>

let score = 0
const values = [1,2,3,4,10]

let votes = {A:0,B:0,C:0,D:0}

/* CHANGE THIS TO YOUR TWITCH NAME */
const client = new tmi.Client({
channels: ["YOUR_CHANNEL_NAME"]
})

client.connect()

client.on('message',(channel,tags,message,self)=>{
message = message.trim().toUpperCase()
if(votes[message] !== undefined){
votes[message]++
}
})

let timer = 30
let timerInterval
const timerEl = document.getElementById("timer")

function startTimer(){
votes = {A:0,B:0,C:0,D:0}
clearInterval(timerInterval)
timer = 30
timerEl.textContent = timer

timerInterval = setInterval(()=>{
timer--
timerEl.textContent = timer

if(timer <=0){
clearInterval(timerInterval)
finishVoting()
}
},1000)
}

const categories = [
{
name:"Python",
questions:[
{value:1,q:"Keyword for function?",choices:["A) func","B) def","C) function","D) define"],correct:"B"},
{value:2,q:"Length function?",choices:["A) size()","B) length()","C) len()","D) count()"],correct:"C"},
{value:3,q:"Comment symbol?",choices:["A) //","B) #","C) --","D) !!"],correct:"B"},
{value:4,q:"Add to list?",choices:["A) add()","B) push()","C) append()","D) insertEnd()"],correct:"C"},
{value:10,q:"Create class?",choices:["A) object","B) struct","C) class","D) type"],correct:"C"}
]
},
{
name:"JavaScript",
questions:[
{value:1,q:"Constant keyword?",choices:["A) const","B) var","C) static","D) fixed"],correct:"A"},
{value:2,q:"Console output?",choices:["A) print()","B) console.log()","C) log()","D) echo()"],correct:"B"},
{value:3,q:"Block scope?",choices:["A) var","B) let","C) define","D) block"],correct:"B"},
{value:4,q:"Comment symbol?",choices:["A) #","B) //","C) --","D) **"],correct:"B"},
{value:10,q:"Parse JSON?",choices:["A) JSON.convert()","B) JSON.parse()","C) parseJSON()","D) JSON.read()"],correct:"B"}
]
},
{
name:"Java",
questions:[
{value:1,q:"Entry method?",choices:["A) start()","B) init()","C) main()","D) run()"],correct:"C"},
{value:2,q:"Inheritance keyword?",choices:["A) extend","B) extends","C) inherit","D) using"],correct:"B"},
{value:3,q:"Scanner package?",choices:["A) java.io","B) java.util","C) java.lang","D) core"],correct:"B"},
{value:4,q:"Prevent override?",choices:["A) const","B) final","C) stop","D) static"],correct:"B"},
{value:10,q:"Language type?",choices:["A) Procedural","B) OOP","C) Functional","D) Assembly"],correct:"B"}
]
},
{
name:"C++",
questions:[
{value:1,q:"IO header?",choices:["A) <stdio.h>","B) <iostream>","C) <stream>","D) <output>"],correct:"B"},
{value:2,q:"cout operator?",choices:["A) >>","B) <<","C) ::","D) ++"],correct:"B"},
{value:3,q:"Dynamic memory?",choices:["A) malloc","B) alloc","C) new","D) create"],correct:"C"},
{value:4,q:"Comment symbol?",choices:["A) //","B) #","C) --","D) ;;"],correct:"A"},
{value:10,q:"Constant keyword?",choices:["A) const","B) fixed","C) static","D) freeze"],correct:"A"}
]
},
{
name:"C#",
questions:[
{value:1,q:"Entry point?",choices:["A) Main()","B) Start()","C) Init()","D) Run()"],correct:"A"},
{value:2,q:"Console output?",choices:["A) Print()","B) Console.WriteLine()","C) echo()","D) log()"],correct:"B"},
{value:3,q:"Console namespace?",choices:["A) Core","B) System","C) Runtime","D) MS"],correct:"B"},
{value:4,q:"Create object?",choices:["A) new","B) make","C) alloc","D) object"],correct:"A"},
{value:10,q:"Comment symbol?",choices:["A) #","B) //","C) --","D) **"],correct:"B"}
]
}
]

const board = document.getElementById("board")

categories.forEach(cat=>{
const c=document.createElement("div")
c.className="category"
c.innerText=cat.name
board.appendChild(c)
})

for(let row=0;row<5;row++){
categories.forEach((cat,i)=>{
const tile=document.createElement("div")
tile.className="tile"
tile.innerText="$"+values[row]
tile.onclick=()=>openQuestion(i,row,tile)
board.appendChild(tile)
})
}

let currentQuestion
let currentValue

function openQuestion(cat,row,tile){
tile.classList.add("used")
currentQuestion = categories[cat].questions[row]
currentValue = currentQuestion.value

document.getElementById("questionText").innerText=currentQuestion.q
document.getElementById("answersText").innerHTML=currentQuestion.choices.join("<br>")
document.getElementById("resultText").innerText=""
document.getElementById("questionScreen").style.display="flex"

startTimer()
}

function finishVoting(){

let winner = Object.keys(votes).reduce((a,b)=>votes[a]>votes[b]?a:b)
let correct = currentQuestion.correct

if(winner === correct){
score += currentValue
document.getElementById("resultText").innerText="Chat chose "+winner+" — CORRECT!"
}else{
score -= currentValue
document.getElementById("resultText").innerText="Chat chose "+winner+" — WRONG! Correct: "+correct
}

updateScore()

setTimeout(()=>{
document.getElementById("questionScreen").style.display="none"
},4000)
}

function updateScore(){
document.getElementById("score").innerText="Score: "+score
}

</script>

</body>
</html>
"""

with open("jeopardy_overlay.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("Overlay created: jeopardy_overlay.html")