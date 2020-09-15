const bat = document.getElementById("bat");
const bowl = document.getElementById("bowl");
const allround = document.getElementById("allround");
const wicket = document.getElementById("wicket");

const batcont = document.querySelector(".bat");
const bowlcont = document.querySelector(".bowl");
const allroundcont = document.querySelector(".allround");
const wicketcont = document.querySelector(".wicket");
const selectt = document.querySelector(".selec");
const check = document.querySelectorAll(".css-checkbox");

const creditBox = document.querySelector(".credi");
const playerBox = document.querySelector(".playerbox");

const playerDiv = document.querySelector('.playerdiv');
const playerdiv2 = document.querySelector('.playerdiv2');

const batno = document.querySelector(".batno");
const bowlno = document.querySelector(".bowlno");
const wicketno = document.querySelector(".wicketno");
const allroundno = document.querySelector(".allroundno");

const overseas = document.querySelector(".overseas");

const continueBtn = document.getElementById("contt");
continueBtn.disabled = true;
const continueBtn2 = document.getElementById("continu");
continueBtn2.disabled = true;

const selectCaptainDiv = document.getElementById('captain');
const selectViceCaptainDiv = document.getElementById('vicecaptain');


bowlcont.style.display = "none";
allroundcont.style.display = "none";
wicketcont.style.display = "none";

bat.addEventListener("click", (e) => {
  batcont.style.display = "block";
  bat.className += " bottom";
  bowl.classList.remove("bottom");
  wicket.classList.remove("bottom");
  allround.classList.remove("bottom");
  bowlcont.style.display = "none";
  allroundcont.style.display = "none";
  wicketcont.style.display = "none";
  selectt.innerHTML = "Select 3-6 Batsman";
});
bowl.addEventListener("click", (e) => {
  batcont.style.display = "none";
  bowlcont.style.display = "block";
  bat.classList.remove("bottom");
  wicket.classList.remove("bottom");
  allround.classList.remove("bottom");
  bowl.className += " bottom";
  allroundcont.style.display = "none";
  wicketcont.style.display = "none";
  selectt.innerHTML = "Select 3-6 Bowler";
});
allround.addEventListener("click", (e) => {
  bowlcont.style.display = "none";
  batcont.style.display = "none";
  bat.classList.remove("bottom");
  wicket.classList.remove("bottom");
  bowl.classList.remove("bottom");
  allround.className += " bottom";
  allroundcont.style.display = "block";
  wicketcont.style.display = "none";
  selectt.innerHTML = "Select 1-4 All Rounders";
});
wicket.addEventListener("click", (e) => {
  bowlcont.style.display = "none";
  allroundcont.style.display = "none";
  bat.classList.remove("bottom");
  bowl.classList.remove("bottom");
  allround.classList.remove("bottom");
  wicket.className += " bottom";
  batcont.style.display = "none";
  wicketcont.style.display = "block";
  selectt.innerHTML = "Select 1-4 Wicket Keeper";
});

check.forEach((ele) => {
  ele.addEventListener("click", (e) => {
    let val = e.target.parentElement.parentElement.children[3];
    let position = e.target.parentElement.parentElement.children[4].innerHTML;
    let country = e.target.parentElement.parentElement.children[5].innerHTML;
    const lis = e.target.parentElement.parentElement.classList;
    let check = 1;
    lis.forEach((elements) => {
      if (elements == "bottom2") {
        check = 0;
      }
    });
    if (check == 1) {
      if (parseInt(creditBox.innerHTML) - parseInt(val.innerHTML) < 0) {
        console.log(e.target.checked);
        e.target.checked = false;
      } else {
        e.target.parentElement.parentElement.className += " bottom2";
        playerBox.innerHTML = parseInt(playerBox.innerHTML) + 1;
        creditBox.innerHTML = parseInt(creditBox.innerHTML) - parseInt(val.innerHTML);
        console.log(e.target.parentElement.parentElement.children[0].children[0].src);
        if (position === "Batsman") {
          batno.innerHTML = parseInt(batno.innerHTML) + 1;
        } else if (position === "Bowler") {
          bowlno.innerHTML = parseInt(bowlno.innerHTML) + 1;
        } else if (position === "Wicket Keeper") {
          wicketno.innerHTML = parseInt(wicketno.innerHTML) + 1;
        } else {
          allroundno.innerHTML = parseInt(allroundno.innerHTML) + 1;
        }
        if (country != "India") {
          overseas.innerHTML = parseInt(overseas.innerHTML) + 1;
        }
      }
      checkcred();
    } else {
      e.target.parentElement.parentElement.classList.remove("bottom2");
      creditBox.innerHTML =
        parseInt(creditBox.innerHTML) + parseInt(val.innerHTML);
      playerBox.innerHTML = parseInt(playerBox.innerHTML) - 1;
      if (position === "Batsman") {
        batno.innerHTML = parseInt(batno.innerHTML) - 1;
      } else if (position === "Bowler") {
        bowlno.innerHTML = parseInt(bowlno.innerHTML) - 1;
      } else if (position === "Wicket Keeper") {
        wicketno.innerHTML = parseInt(wicketno.innerHTML) - 1;
      } else {
        allroundno.innerHTML = parseInt(allroundno.innerHTML) - 1;
      }
      if (country != "India") {
        overseas.innerHTML = parseInt(overseas.innerHTML) - 1;
      }
      checkcred();
    }
    for (let i = 1; i <= 11; i++) {
      if (i <= parseInt(playerBox.innerHTML)) {
        let boxx = document.querySelector(`.box${i}`);
        boxx.classList.remove("bg-white");
        boxx.classList.add("bg-success");
      } else {
        let box2 = document.querySelector(`.box${i}`);
        box2.classList.remove("bg-success");
        box2.classList.add("bg-white");
      }
    }
    if (parseInt(playerBox.innerHTML) === 11) {
      continueBtn.disabled = false;
      continueBtn2.disabled = false;
      checkcred();
    } else {
      continueBtn.disabled = true;
      continueBtn2.disabled = true;
    }
  });
});
function checkcred() {
  check.forEach((element) => {
    let vals = element.parentElement.parentElement.children[3].innerHTML;
    const listt = element.parentElement.parentElement.classList;
    let check = 1;
    listt.forEach((elements) => {
      if (elements == "bottom2") {
        check = 0;
      }
    });
    if (check == 0) {
    } else {
      if (parseInt(playerBox.innerHTML) === 11) {
        element.parentElement.parentElement.className += " bottom3";
        element.parentElement.parentElement.style.opacity = 0.4;
        element.disabled = true;
      } else {
        if (
          parseInt(batno.innerHTML) == 6 ||
          parseInt(bowlno.innerHTML) == 6 ||
          parseInt(wicketno.innerHTML) == 4 ||
          parseInt(allroundno.innerHTML) == 4
        ) {
          if (parseInt(batno.innerHTML) == 6) {
            if (
              element.parentElement.parentElement.children[4].innerHTML ===
              "Batsman"
            ) {
              element.parentElement.parentElement.className += " bottom3";
              element.parentElement.parentElement.style.opacity = 0.4;
              element.disabled = true;
            }
          }
          if (parseInt(bowlno.innerHTML) == 6) {
            if (
              element.parentElement.parentElement.children[4].innerHTML ===
              "Bowler"
            ) {
              element.parentElement.parentElement.className += " bottom3";
              element.parentElement.parentElement.style.opacity = 0.4;
              element.disabled = true;
            }
          }
          if (parseInt(wicketno.innerHTML) == 4) {
            if (
              element.parentElement.parentElement.children[4].innerHTML ===
              "Wicket Keeper"
            ) {
              element.parentElement.parentElement.className += " bottom3";
              element.parentElement.parentElement.style.opacity = 0.4;
              element.disabled = true;
            }
          }
          if (parseInt(allroundno.innerHTML) == 4) {
            if (
              element.parentElement.parentElement.children[4].innerHTML ===
              "All Rounder"
            ) {
              element.parentElement.parentElement.className += " bottom3";
              element.parentElement.parentElement.style.opacity = 0.4;
              element.disabled = true;
            }
          }
        } else {
          if (parseInt(creditBox.innerHTML) - parseInt(vals) >= 0) {
            element.parentElement.parentElement.classList.remove("bottom3");
            element.parentElement.parentElement.style.opacity = 1;
            element.disabled = false;
          } else {
            element.parentElement.parentElement.className += " bottom3";
            element.parentElement.parentElement.style.opacity = 0.4;
            element.disabled = true;
          }
        }
        if (parseInt(overseas.innerHTML) == 4) {
          if (
            element.parentElement.parentElement.children[5].innerHTML ===
            "India"
          ) {
          } else {
            element.parentElement.parentElement.className += " bottom3";
            element.parentElement.parentElement.style.opacity = 0.4;
            element.disabled = true;
          }
        }
      }
    }
  });
}

continueBtn2.addEventListener('click',myfunccc);

function myfunccc(){
  const inputs = document.querySelectorAll('.css-checkbox');
  inputs.forEach(inps => {
    if(inps.checked==true){
    let abc = document.createElement('option');
    abc.innerHTML = `${inps.parentElement.parentElement.children[1].innerHTML}`;
    abc.value = `${parseInt(inps.parentElement.parentElement.children[6].innerHTML)}`;
    selectCaptainDiv.appendChild(abc);
    }
  });
  inputs.forEach(inpss => {
    if(inpss.checked==true){
    let def = document.createElement('option');
    def.innerHTML = `${inpss.parentElement.parentElement.children[1].innerHTML}`;
    def.value = `${parseInt(inpss.parentElement.parentElement.children[6].innerHTML)}`;
    selectViceCaptainDiv.appendChild(def);
    }
  });
}

continueBtn.addEventListener('click',(e)=>{
  e.preventDefault();
  if((e.target.parentElement.children[1].children[1].value) === (e.target.parentElement.children[2].children[1].value) ){
    document.querySelector('#myalert').classList.remove('hidden');
    document.querySelector('#myalert').innerHTML = "Please Choose Captain and Vice-Captain Different Players *";
  }else{
    document.querySelector('#myform').submit();
  }
});