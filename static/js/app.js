const bat = document.getElementById('bat');
const bowl = document.getElementById('bowl');
const allround = document.getElementById('allround');
const wicket = document.getElementById('wicket');

const batcont = document.querySelector('.bat');
const bowlcont = document.querySelector('.bowl');
const allroundcont = document.querySelector('.allround');
const wicketcont = document.querySelector('.wicket');
const selectt = document.querySelector('.selec');
const check = document.querySelectorAll('.css-checkbox');

bowlcont.style.display="none";
allroundcont.style.display="none";
wicketcont.style.display="none";


bat.addEventListener('click',(e)=>{
    batcont.style.display="block";
    bat.className +=" bottom";
    bowl.classList.remove('bottom');
    wicket.classList.remove('bottom');
    allround.classList.remove('bottom');
    bowlcont.style.display="none";
    allroundcont.style.display="none";
    wicketcont.style.display="none";
    selectt.innerHTML = "Select 4-5 Batsman";
});
bowl.addEventListener('click',(e)=>{
    batcont.style.display="none";
    bowlcont.style.display="block";
    bat.classList.remove('bottom');
    wicket.classList.remove('bottom');
    allround.classList.remove('bottom');
    bowl.className +=" bottom";
    allroundcont.style.display="none";
    wicketcont.style.display="none";
    selectt.innerHTML = "Select 4-5 Bowler";
});
allround.addEventListener('click',(e)=>{
    bowlcont.style.display="none";
    batcont.style.display="none";
    bat.classList.remove('bottom');
    wicket.classList.remove('bottom');
    bowl.classList.remove('bottom');
    allround.className +=" bottom";
    allroundcont.style.display="block";
    wicketcont.style.display="none";
    selectt.innerHTML = "Select 4-5 All Rounders";
});
wicket.addEventListener('click',(e)=>{
    bowlcont.style.display="none";
    allroundcont.style.display="none";
    bat.classList.remove('bottom');
    bowl.classList.remove('bottom');
    allround.classList.remove('bottom');
    wicket.className +=" bottom";
    batcont.style.display="none";
    wicketcont.style.display="block";
    selectt.innerHTML = "Select 1 Wicket Keeper";
});

check.forEach(ele => {
    ele.addEventListener('click',(e)=>{   
        const lis = e.target.parentElement.parentElement.classList;
        let check = 1;
        lis.forEach(elements => {
            if(elements == "bottom2"){
                check = 0;
            }
        });
        if(check == 1){
            e.target.parentElement.parentElement.className += " bottom2";
        }else{
            e.target.parentElement.parentElement.classList.remove("bottom2");
        }
    });
});