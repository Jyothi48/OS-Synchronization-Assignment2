import json
import random
import threading
import time
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "generated_html" / "dining_philosophers_semaphore.html"
EVENTS = []
EVENT_LOCK = threading.Lock()


def record(message, states):
    """Save a real state/event snapshot while holding a log lock."""
    with EVENT_LOCK:
        EVENTS.append({"time": round(time.time(), 3), "message": message, "states": dict(states)})



def write_html(title, state_labels, final_note):
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    payload = json.dumps(EVENTS)
    labels = json.dumps(state_labels)

    html = r'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>TITLE_PLACEHOLDER</title>

<style>
*{box-sizing:border-box}
body{font-family:system-ui,Arial,sans-serif;margin:0;background:#f1f5fb;color:#1d2939}
header{background:#17324d;color:white;padding:22px 5%}
main{max-width:1100px;margin:24px auto;padding:0 16px}
.panel{background:white;border-radius:14px;padding:20px;margin:16px 0;box-shadow:0 3px 14px #172b4d12}
button{border:0;border-radius:8px;padding:10px 15px;margin:4px;background:#245b86;color:white;cursor:pointer}
button:hover{background:#17324d}
#message{font-size:1.05rem;font-weight:600}
.small{color:#526477;font-size:.9rem}

.table-stage{position:relative;width:100%;max-width:570px;height:460px;margin:20px auto}
.round-table{
 position:absolute;width:230px;height:230px;left:50%;top:50%;
 transform:translate(-50%,-50%);border-radius:50%;
 background:#d9c2a1;border:9px solid #a7835b;
 box-shadow:inset 0 0 0 5px #eadcc7,0 8px 18px #00000018;
 display:flex;align-items:center;justify-content:center;
 text-align:center;color:#49321f;font-weight:bold;font-size:1.2rem
}
.seat{
 position:absolute;width:130px;min-height:76px;padding:10px 5px;
 text-align:center;border:2px solid #cbd5e1;border-radius:14px;
 background:#f8fafc;z-index:2
}
.seat strong{display:block;font-size:.95rem;margin-bottom:5px}
.status{display:inline-block;padding:4px 8px;border-radius:20px;font-size:.78rem;background:#e2e8f0}
.thinking{border-color:#94a3b8;background:#f1f5f9}
.hungry{border-color:#e9a23b;background:#fff7e6}
.hungry .status{background:#fde5b3}
.eating{border-color:#16a34a;background:#ecfdf3}
.eating .status{background:#bbf7d0}

.p0{top:0;left:50%;transform:translateX(-50%)}
.p1{right:0;top:50%;transform:translateY(-50%)}
.p2{bottom:0;left:50%;transform:translateX(-50%)}
.p3{left:0;top:50%;transform:translateY(-50%)}

.fork{
 position:absolute;z-index:3;width:105px;padding:7px 3px;
 text-align:center;border:2px solid #cbd5e1;border-radius:10px;
 background:#f8fafc;font-size:.76rem;overflow-wrap:anywhere
}
.fork strong{display:block}
.fork.available{border-color:#94a3b8}
.fork.held{background:#dbeafe;border-color:#3b82f6}
.f0{top:78px;right:65px}
.f1{bottom:78px;right:65px}
.f2{bottom:78px;left:65px}
.f3{top:78px;left:65px}

.legend{color:#526477;font-size:.9rem}
.timeline-wrap{overflow-x:auto}
table{width:100%;min-width:650px;border-collapse:collapse}
th,td{text-align:left;padding:10px;border-bottom:1px solid #e5eaf0;vertical-align:top}
th{background:#f5f8fc}
tbody tr{cursor:pointer}
tbody tr:hover{background:#f1f7ff}
.current{outline:2px solid #4388c5;background:#eef7ff}

@media(max-width:520px){
 .table-stage{transform:scale(.84);transform-origin:top center;width:570px;left:50%;margin-left:-285px;margin-bottom:-65px}
 .panel{overflow:hidden}
 main{padding:0 10px}
}
</style>
</head>

<body>
<header>
<h1>TITLE_PLACEHOLDER</h1>
<p>Execution-based semaphore synchronization simulation.</p>
</header>

<main>
<section class="panel">
<h2>Dining Philosophers Simulation</h2>
<p id="message">Press Play to view recorded events.</p>

<button id="play">Play</button>
<button id="pause">Pause</button>
<button id="prev">Previous</button>
<button id="next">Next</button>
<button id="reset">Reset</button>

<p class="small" id="counter"></p>

<div class="table-stage">
 <div class="round-table">DINING<br>TABLE</div>

 <div class="seat p0" id="p0"><strong>Philosopher 0</strong><span class="status">Thinking</span></div>
 <div class="seat p1" id="p1"><strong>Philosopher 1</strong><span class="status">Thinking</span></div>
 <div class="seat p2" id="p2"><strong>Philosopher 2</strong><span class="status">Thinking</span></div>
 <div class="seat p3" id="p3"><strong>Philosopher 3</strong><span class="status">Thinking</span></div>

 <div class="fork f0" id="f0"><strong>Fork 0</strong>Available</div>
 <div class="fork f1" id="f1"><strong>Fork 1</strong>Available</div>
 <div class="fork f2" id="f2"><strong>Fork 2</strong>Available</div>
 <div class="fork f3" id="f3"><strong>Fork 3</strong>Available</div>
</div>

<p class="legend">
Green = Eating | Yellow = Hungry / Waiting | Blue fork = In use
</p>
</section>

<section class="panel">
<h2>Execution Event Timeline</h2>
<p class="small">Events and state snapshots recorded during the actual program execution.</p>
<div class="timeline-wrap">
<table>
<thead><tr><th>#</th><th>Event</th><th>State Snapshot</th></tr></thead>
<tbody id="events"></tbody>
</table>
</div>
</section>

<section class="panel">
<h2>Notes</h2>
<p>FINAL_NOTE_PLACEHOLDER</p>
</section>
</main>

<script>
const events=EVENTS_PLACEHOLDER;
const labels=LABELS_PLACEHOLDER;
let index=0,timer=null;

const esc=s=>String(s).replace(/[&<>"']/g,c=>({
 '&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'
}[c]));

function pause(){
 if(timer!==null){clearInterval(timer);timer=null;}
}

function render(){
 if(!events.length)return;

 const e=events[index];
 document.getElementById('message').textContent=e.message;
 document.getElementById('counter').textContent=
  `Event ${index+1} of ${events.length}`;

 // Update philosopher seats from the recorded snapshot.
 for(let i=0;i<4;i++){
  const seat=document.getElementById('p'+i);
  const status=seat.querySelector('.status');
  const value=e.states['Philosopher '+i]||'Thinking';

  status.textContent=value;
  seat.classList.remove('thinking','hungry','eating');

  if(value.toLowerCase().includes('eating')){
   seat.classList.add('eating');
  }else if(value.toLowerCase().includes('hungry')){
   seat.classList.add('hungry');
  }else{
   seat.classList.add('thinking');
  }
 }

 // Display fork availability and ownership.
 for(let i=0;i<4;i++){
  const fork=document.getElementById('f'+i);
  const value=e.states['Fork '+i]||'Available';

  fork.classList.remove('available','held');

  if(value.startsWith('Held by')){
   fork.classList.add('held');
   fork.innerHTML='<strong>Fork '+i+'</strong>'+esc(value);
  }else{
   fork.classList.add('available');
   fork.innerHTML='<strong>Fork '+i+'</strong>Available';
  }
 }

 document.querySelectorAll('#events tr').forEach((tr,i)=>{
  tr.classList.toggle('current',i===index);
 });
}

function step(n){
 index=Math.max(0,Math.min(events.length-1,index+n));
 render();
}

const tbody=document.getElementById('events');

events.forEach((e,i)=>{
 const tr=document.createElement('tr');

 tr.innerHTML='<td>'+(i+1)+'</td>'+
  '<td>'+esc(e.message)+'</td>'+
  '<td>'+esc(Object.entries(e.states)
   .map(([k,v])=>k+': '+v).join(' | '))+'</td>';

 tr.addEventListener('click',()=>{
  pause();
  index=i;
  render();
 });

 tbody.appendChild(tr);
});

document.getElementById('play').onclick=()=>{
 pause();

 if(index>=events.length-1){
  index=0;
  render();
 }

 timer=setInterval(()=>{
  if(index>=events.length-1){
   pause();
   return;
  }
  step(1);
 },1000);
};

document.getElementById('pause').onclick=pause;
document.getElementById('next').onclick=()=>{pause();step(1)};
document.getElementById('prev').onclick=()=>{pause();step(-1)};
document.getElementById('reset').onclick=()=>{
 pause();
 index=0;
 render();
};

render();
</script>
</body>
</html>'''

    html = (
        html.replace('TITLE_PLACEHOLDER', escape(title))
        .replace('FINAL_NOTE_PLACEHOLDER', escape(final_note))
        .replace('EVENTS_PLACEHOLDER', payload)
        .replace('LABELS_PLACEHOLDER', labels)
    )

    OUTPUT.write_text(html, encoding='utf-8')
    print(f"HTML simulation generated: {OUTPUT}")


N = 4
forks = [threading.Semaphore(1) for _ in range(N)]
room = threading.Semaphore(N - 1)  # At most three philosophers compete for forks.
states = {f"Philosopher {i}": "Thinking" for i in range(N)}
states.update({f"Fork {i}": "Available" for i in range(N)})


def philosopher(i):
    left, right = i, (i + 1) % N
    time.sleep(random.uniform(0.02, 0.14))
    states[f"Philosopher {i}"] = "Hungry / waiting"
    record(f"Philosopher {i} becomes hungry and waits for a seat permit.", states)
    room.acquire()
    forks[left].acquire()
    states[f"Fork {left}"] = f"Held by Philosopher {i}"
    record(f"Philosopher {i} picks up Fork {left}.", states)
    forks[right].acquire()
    states[f"Fork {right}"] = f"Held by Philosopher {i}"
    states[f"Philosopher {i}"] = "Eating"
    record(f"Philosopher {i} has both forks and starts eating.", states)
    time.sleep(random.uniform(0.08, 0.16))
    forks[right].release(); states[f"Fork {right}"] = "Available"
    forks[left].release(); states[f"Fork {left}"] = "Available"
    states[f"Philosopher {i}"] = "Thinking again"
    record(f"Philosopher {i} releases both forks and finishes eating.", states)
    room.release()


if __name__ == "__main__":
    random.seed(21)
    record("Simulation started; all four philosophers are thinking and all forks are free.", states)
    threads = [threading.Thread(target=philosopher, args=(i,)) for i in range(N)]
    for t in threads: t.start()
    for t in threads: t.join()
    record("All four philosophers have completed one eating cycle.", states)
    write_html("Dining Philosophers: Semaphore Solution", list(states), "Exactly four philosophers and four forks are used. The room semaphore allows at most three philosophers to compete for forks simultaneously, breaking circular wait and preventing deadlock. Starvation is possible in principle because semaphore scheduling is not guaranteed to be fair.")
