// 1. Mouse Move Parallax Logic for Floating Orbs
document.addEventListener('mousemove', (e) => {
    const orb1 = document.getElementById('orb1');
    const orb2 = document.getElementById('orb2');
    
    if (orb1 && orb2) {
        const moveX = (e.clientX - window.innerWidth / 2) * 0.04;
        const moveY = (e.clientY - window.innerHeight / 2) * 0.04;
        
        orb1.style.transform = `translate(${moveX}px, ${moveY}px)`;
        orb2.style.transform = `translate(${-moveX}px, ${-moveY}px)`;
    }
});

// 2. Deep Interactive 3D Tilt Effect for Main Container Box
const card = document.getElementById('main-container');
if (card) {
    document.addEventListener('mousemove', (e) => {
        const xAxis = (window.innerWidth / 2 - e.clientX) / 50;
        const yAxis = (window.innerHeight / 2 - e.clientY) / 50;
        card.style.transform = `rotateY(${xAxis}deg) rotateX(${yAxis}deg)`;
    });

    // Reset positions smoothly when mouse exits window boundary
    document.addEventListener('mouseleave', () => {
        card.style.transform = `rotateY(0deg) rotateX(0deg)`;
    });
}

// 3. Falling/Drifting Micro Sparkles Canvas Animation
const canvas = document.getElementById('sparkle-canvas');
if (canvas) {
    const ctx = canvas.getContext('2d');
    let sparkles = [];

    function resizeCanvas() {
        canvas.width = window.innerWidth;
        canvas.height = window.innerHeight;
    }
    window.addEventListener('resize', resizeCanvas);
    resizeCanvas();

    class Sparkle {
        constructor() {
            this.x = Math.random() * canvas.width;
            this.y = Math.random() * canvas.height;
            this.size = Math.random() * 2 + 0.5;
            this.speedY = Math.random() * 0.3 + 0.1;
            this.opacity = Math.random() * 0.5 + 0.2;
        }
        update() {
            this.y -= this.speedY;
            if (this.y < 0) {
                this.y = canvas.height;
                this.x = Math.random() * canvas.width;
            }
        }
        draw() {
            ctx.fillStyle = `rgba(255, 255, 255, ${this.opacity})`;
            ctx.beginPath();
            ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2);
            ctx.fill();
        }
    }

    function initSparkles() {
        sparkles = [];
        for (let i = 0; i < 40; i++) {
            sparkles.push(new Sparkle());
        }
    }

    function animateSparkles() {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        sparkles.forEach(sparkle => {
            sparkle.update();
            sparkle.draw();
        });
        requestAnimationFrame(animateSparkles);
    }

    initSparkles();
    animateSparkles();
}