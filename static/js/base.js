//NAVBAR HANDLING

var menuBtn = false;
document.getElementById('menuBtn').addEventListener('click', menu);
menuLink = document.getElementsByClassName('menuLink');
const wait = (ms) => new Promise(resolve => setTimeout(resolve, ms))

function menu() {
    if (menuBtn === false) {
        menuBtn = true;
        document.getElementById('menuBtnLine1').style.width = '0px';
        document.getElementById('menuBtnLine2').style.width = '1.5em';
        document.getElementById('menu').style.opacity = '1';
        document.getElementById('menu').style.pointerEvents = 'all';
        document.getElementById('menu').style.zIndex = '999';
        document.getElementById('menuBtn').style.height = '4px';
        document.getElementById('navbar').style.boxShadow = '0px 5px 15px rgba(0, 0, 0, 0)';
        const loop = async () => {
            for (var i = 0; i < menuLink.length; i++) {
                menuLink[i].style.opacity = '1';
                menuLink[i].style.transform = 'translateX(0px)';
                await wait(150);
            }
        }
        loop();
    }
    else {
        menuBtn = false;
        document.getElementById('menuBtnLine1').style.width = '2em';
        document.getElementById('menuBtnLine2').style.width = '1.2em';
        document.getElementById('menu').style.opacity = '0';
        document.getElementById('menu').style.pointerEvents = 'none';
        document.getElementById('menu').style.zIndex = '-999';
        document.getElementById('menuBtn').style.height = '10px';
        document.getElementById('navbar').style.boxShadow = '0px 5px 15px rgba(0, 0, 0, 0.05)';
        for (var i = 0; i < menuLink.length; i++) {
            menuLink[i].style.opacity = '0';
            menuLink[i].style.transform = 'translateX(-100px)';
        }
    }
}

window.onscroll = function (ev) {
    if ((window.innerHeight + window.scrollY) >= (document.body.offsetHeight - 10)) {
        document.getElementById('footer').style.transform = 'scale(1)';
    }
    else {
        document.getElementById('footer').style.transform = 'scale(0.9)';
    }
};

window.onscroll = function (ev) {
    if (window.scrollY >= 10) {
        document.getElementById('navbar').style.boxShadow = '0px 5px 15px rgba(0, 0, 0, 0.05)';
    }
    else {
        document.getElementById('navbar').style.boxShadow = '0px 5px 15px rgba(0, 0, 0, 0)';
    }
};




//MENU HANDLING

document.getElementById('menuLink1').addEventListener('click', event => {
    document.getElementById('menuLink1').style.color = 'black';
    document.getElementById('menuLink2').style.color = 'lightgray';
    document.getElementById('menuLink3').style.color = 'lightgray';
    document.getElementById('menuLink4').style.color = 'lightgray';
    document.getElementById('menuImg1').style.opacity = '1';
    document.getElementById('menuImg2').style.opacity = '0';
    document.getElementById('menuImg3').style.opacity = '0';
    document.getElementById('menuImg4').style.opacity = '0';
    document.getElementById('menuImg1').style.pointerEvents = 'all';
    document.getElementById('menuImg2').style.pointerEvents = 'none';
    document.getElementById('menuImg3').style.pointerEvents = 'none';
    document.getElementById('menuImg4').style.pointerEvents = 'none';
})

document.getElementById('menuLink2').addEventListener('click', event => {
    document.getElementById('menuLink1').style.color = 'lightgray';
    document.getElementById('menuLink2').style.color = 'black';
    document.getElementById('menuLink3').style.color = 'lightgray';
    document.getElementById('menuLink4').style.color = 'lightgray';
    document.getElementById('menuImg1').style.opacity = '0';
    document.getElementById('menuImg2').style.opacity = '1';
    document.getElementById('menuImg3').style.opacity = '0';
    document.getElementById('menuImg4').style.opacity = '0';
    document.getElementById('menuImg1').style.pointerEvents = 'none';
    document.getElementById('menuImg2').style.pointerEvents = 'all';
    document.getElementById('menuImg3').style.pointerEvents = 'none';
    document.getElementById('menuImg4').style.pointerEvents = 'none';
})

document.getElementById('menuLink3').addEventListener('click', event => {
    document.getElementById('menuLink1').style.color = 'lightgray';
    document.getElementById('menuLink2').style.color = 'lightgray';
    document.getElementById('menuLink3').style.color = 'black';
    document.getElementById('menuLink4').style.color = 'lightgray';
    document.getElementById('menuImg1').style.opacity = '0';
    document.getElementById('menuImg2').style.opacity = '0';
    document.getElementById('menuImg3').style.opacity = '1';
    document.getElementById('menuImg4').style.opacity = '0';
    document.getElementById('menuImg1').style.pointerEvents = 'none';
    document.getElementById('menuImg2').style.pointerEvents = 'none';
    document.getElementById('menuImg3').style.pointerEvents = 'all';
    document.getElementById('menuImg4').style.pointerEvents = 'none';
})

document.getElementById('menuLink4').addEventListener('click', event => {
    document.getElementById('menuLink1').style.color = 'lightgray';
    document.getElementById('menuLink2').style.color = 'lightgray';
    document.getElementById('menuLink3').style.color = 'lightgray';
    document.getElementById('menuLink4').style.color = 'black';
    document.getElementById('menuImg1').style.opacity = '0';
    document.getElementById('menuImg2').style.opacity = '0';
    document.getElementById('menuImg3').style.opacity = '0';
    document.getElementById('menuImg4').style.opacity = '1';
    document.getElementById('menuImg1').style.pointerEvents = 'none';
    document.getElementById('menuImg2').style.pointerEvents = 'none';
    document.getElementById('menuImg3').style.pointerEvents = 'none';
    document.getElementById('menuImg4').style.pointerEvents = 'all';
})



//TEST DATA

// for (var i=1; i < document.getElementsByClassName('goToBagBtn').length + 1; i++) {
//     if (i === 3) {
//         console.log('Element ', i, ' not styled');
//         document.getElementsByClassName('goToBagBtn')[i].style.color = 'black';
//         document.getElementsByClassName('goToBagBtn')[i].style.opacity = '1';
//         document.getElementsByClassName('goToBagBtn')[i].style.pointerEvents = 'all';
//     }
//     else {
//         console.log('Element ', i, ' styled');
//         document.getElementsByClassName('goToBagBtn')[i].style.color = 'lightgray';
//         document.getElementsByClassName('goToBagBtn')[i].style.opacity = '0';
//         document.getElementsByClassName('goToBagBtn')[i].style.pointerEvents = 'none';
//     }
// }