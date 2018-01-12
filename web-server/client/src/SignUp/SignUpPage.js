import React, {PropTypes} from 'react';
import Auth from '../Auth/Auth';
import SignUpForm from './SignUpForm';

class SignUpPage extends React.Component{
    constructor(props,context){
        super(props,context);
    

        //set the initial component state

        this.state = {
            errors: {},
            user:{
                email:'',
                password:'',
                confirm_password:''
            }
        };

        this.processForm = this.processForm.bind(this);
        this.changeUser = this.changeUser.bind(this);
    }
    //pre-submission 
    processForm(event){
        event.preventDefault();

        const email = this.state.user.email;
        const password = this.state.user.password;
        const confirm_password = this.state.user.confirm_password;
        if(password !== confirm_password){
            return;
        }
        //TODO; POST login data
        fetch('http://localhost:3000/auth/signup',{
            method:'POST',
            headers:{
                'Accept':'application/json',
                'Content-Type':'application/json',
            },
            body:JSON.stringify({
                email:email,
                password:password
            })
        }).then(response=>{
            if(response.status === 200 ){
                this.setState({
                    errors:{}
                });
                //change the current URL TO /LOGIN 
                this.context.router.replace('/login');
            }
            else{
                response.json().then(function(json) {
                    console.log(json);
                    const errors = json.errors ? json.errors : {};
                    errors.summary = json.message;
                    this.setState({errors});
                }.bind(this));
            }
        });
    }

    changeUser(event){
        const field = event.target.name;
        const user = this.state.user;//this 'this' not indicates this loginpage, but the event
        user[field] = event.target.value;
        //user['email'] = '123@123.com
        //user['password'] = 12312
        //usesr['confirm-passowrd] = '12312'
        this.setState({user});

        if(this.state.user.password !== this.state.user.confirm_password){
            const errors = this.state.errors;
            errors.password = "Password and confirm_password don't match";
            this.setState({errors});
        }
        else{
            const errors = this.state.errors;
            errors.password = '';
            this.setState({errors});
        }
    }

    render(){
        //not this.processForm() because it wants value not execute this function
        return(
            <SignUpForm onSubmit = {this.processForm}
                        onChange = {this.changeUser}
                        errors = {this.state.errors}
                        user = {this.state.user}
            />
        );
    }

}

SignUpPage.contextTypes = {
    router:PropTypes.object.isRequired
};

export default SignUpPage;