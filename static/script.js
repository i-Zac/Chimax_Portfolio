// Sticky Navigation Menu JS Code
let nav = document.querySelector("nav");
let scrollBtn = document.querySelector(".scroll-button a");
console.log(scrollBtn);
let val;
window.onscroll = function() {
  if(document.documentElement.scrollTop > 20){
    nav.classList.add("sticky");
    scrollBtn.style.display = "block";
  }else{
    nav.classList.remove("sticky");
    scrollBtn.style.display = "none";
  }

}

// Side NavIgation Menu JS Code
let body = document.querySelector("body");
let navBar = document.querySelector(".navbar");
let menuBtn = document.querySelector(".menu-btn");
let cancelBtn = document.querySelector(".cancel-btn");
menuBtn.onclick = function(){
  navBar.classList.add("active");
  menuBtn.style.opacity = "0";
  menuBtn.style.pointerEvents = "none";
  body.style.overflow = "hidden";
  scrollBtn.style.pointerEvents = "none";
}
cancelBtn.onclick = function(){
  navBar.classList.remove("active");
  menuBtn.style.opacity = "1";
  menuBtn.style.pointerEvents = "auto";
  body.style.overflow = "auto";
  scrollBtn.style.pointerEvents = "auto";
}

// Side Navigation Bar Close While We Click On Navigation Links
let navLinks = document.querySelectorAll(".menu li a");
for (var i = 0; i < navLinks.length; i++) {
  navLinks[i].addEventListener("click" , function() {
    navBar.classList.remove("active");
    menuBtn.style.opacity = "1";
    menuBtn.style.pointerEvents = "auto";
  });
}


// Dynamically open the modal and configure buttons
function openPDFModal(pdfList) {
  const modal = document.getElementById("pdfModal");
  const iframe = document.getElementById("pdfFrame");
  const controls = document.getElementById("pdfControls");

  // Reset buttons and initial PDF
  controls.innerHTML = "";

  if (Array.isArray(pdfList) && pdfList.length > 0) {
    iframe.src = pdfList[0]; // Show first PDF by default

    pdfList.forEach((pdfPath, i) => {
      const btn = document.createElement("button");
      btn.textContent = i === 0 ? "Copy 1" : "Copy 2";
      btn.onclick = () => { iframe.src = pdfPath };
      controls.appendChild(btn);
    });
  } else if (typeof pdfList === "string") {
    iframe.src = pdfList;
  }

  modal.style.display = "block";
}

// Close modal
document.querySelector(".close-btn").onclick = function () {
  document.getElementById("pdfModal").style.display = "none";
  document.getElementById("pdfFrame").src = "";
};

window.onclick = function (e) {
  const modal = document.getElementById("pdfModal");
  if (e.target == modal) {
    modal.style.display = "none";
    document.getElementById("pdfFrame").src = "";
  }
};

// CHANGED: Get modal and elements
const modal = document.getElementById("projectModal");
const modalTitle = document.getElementById("modalTitle");
const pdfViewer = document.getElementById("pdfViewer");
const closeBtn = modal.querySelector(".close-btn");

// CHANGED: Attach click to all project buttons
document.querySelectorAll(".view-project-btn").forEach(button => {
  button.addEventListener("click", () => {
    const pdfFile = button.getAttribute("data-pdf");
    const title = button.getAttribute("data-title");

    // CHANGED: Update modal content
    modalTitle.textContent = title;
    pdfViewer.src = `${pdfFile}#toolbar=0&navpanes=0&scrollbar=0`; // disable download/print
    modal.style.display = "block";
  });
});

// CHANGED: Close modal
closeBtn.addEventListener("click", () => {
  modal.style.display = "none";
  pdfViewer.src = ""; // clear iframe
});

// Optional: Click outside to close
window.addEventListener("click", (e) => {
  if (e.target === modal) {
    modal.style.display = "none";
    pdfViewer.src = "";
  }
});
