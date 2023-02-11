gsap.registerPlugin(ScrollTrigger);
const tl = gsap.timeline();
tl.to(".wrapper",5,{x:-window.innerWidth})
.from(".section2 h2",5,{opacity:0,scale:3})

ScrollTrigger.create({
    animation:tl,
    trigger:".wrapper",
    start:"center center",
    end:"+=4000",
    scrub:true,
    pin:true

})