const usernameField=document.querySelector('#usernameField')
const feedBackArea=document.querySelector('.invalid-feedback')

usernameField.classList.remove('is_invalid')
feedBackArea.style.display='none'
// feedBackArea.innerHTML=`<p>${data.username_error}</p>`

usernameField.addEventListener('keyup', (e) => {
  console.log('777',777)
  const usernameVal = e.target.value


  if(usernameVal.length>0){
    fetch('/authentication/validate-username',{
      body:JSON.stringify({username:usernameVal}),
      method:'POST',
    })
      .then(res=>res.json())
      .then(data=>{
        console.log('data',data)
        if(data.username_error){
          usernameField.classList.add('is_invalid')
          feedBackArea.style.display='block'
          feedBackArea.innerHTML=`<p>${data.username_error}</p>`
        }
    })
  }
})