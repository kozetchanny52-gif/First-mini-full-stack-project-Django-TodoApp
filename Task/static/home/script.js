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