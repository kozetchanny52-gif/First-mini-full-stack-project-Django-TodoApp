const popup_forms=document.querySelectorAll(".update-task-form-popup")
const update_tasks=document.querySelectorAll(".update-task")
const container_tasks=document.querySelector(".container_tasks")
update_tasks.forEach((update_task,index)=>{
    update_task.addEventListener("click",()=>{  
        popup_forms[index].style.display="block"})   
})
close_buttons=document.querySelectorAll("#close-button")
close_buttons.forEach((close_button,index)=>{
   close_button.addEventListener("click",()=>{
    popup_forms[index].style.display="none"
    container_tasks.style.animation="none"
})
})
document.querySelectorAll(".toggle-password").forEach((toggle)=>{
    toggle.addEventListener("click",()=>{
        const password_input=toggle.previousElementSibling
        const icon=toggle.querySelector("i")
        if (!password_input) return
        const show_password=password_input.type === "password"
        password_input.type=show_password ? "text" : "password"
        if (icon) {
            icon.classList.toggle("bi-eye",!show_password)
            icon.classList.toggle("bi-eye-slash",show_password)
        }
        toggle.setAttribute("aria-label",show_password ? "Hide password" : "Show password")
    })
})