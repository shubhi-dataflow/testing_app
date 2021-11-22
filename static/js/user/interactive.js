// Fetch Components
try{
    const passwordEye = document.querySelector(`.password-eye`);
    const passwordInput = document.querySelector(`[name='password']`);

    let passwordState = false;

    passwordEye.addEventListener('click', ()=>{
        console.log('work');
        if(passwordState){
            passwordEye.innerHTML = `<i class="fas fa-eye-slash"></i>`;
            passwordEye.setAttribute('title', 'Hide Password');
            passwordInput.setAttribute('type', 'password');
            passwordState = false;
        }else{
            passwordEye.innerHTML = `<i class="fas fa-eye"></i>`;
            passwordEye.setAttribute('type', 'Show Password');
            passwordInput.setAttribute('type', 'text');
            passwordState = true;
        }
    });

    // Logging In
    const loginForm = document.querySelector('#loginForm'),
          loginBtn = loginForm.querySelector('#loginBtn');

    loginForm.addEventListener('submit', () => {
        loginBtn.innerHTML = `<i class="fas fa-circle-notch load-icon"></i> Logging in`;
    });

}catch(err){}

// Instruction Components
try{
    // Declaration View check
    const declaration = document.querySelector('#declartion');
    const startBtn = document.querySelector('.start-test');
    // Continue/Start
    const startDiv = document.querySelector('.start-test-info');
    const cancelNo = document.querySelector('.cancel-no');

    const declarationChange = (e) => {
        const agreed = e.target.checked;
        startBtn.disabled = !agreed;

        if (agreed) {
            return startBtn.addEventListener('click', openStartDiv);
        }

        return startBtn.removeEventListener('click', openStartDiv)
    }

    const openStartDiv = () => {
        startDiv.style.display = 'flex';
    }

    declaration.addEventListener('change', declarationChange)
    
    cancelNo.addEventListener('click', (e)=>{
        startDiv.style.display = 'none';
    });

}catch(err){
    console.log('err');
}

