class Auth {
    /**
     * Authenticate a user, Save a token string in localStorage. web server allocate token not backend server
     * @param {*} token 
     * @param {*} email 
     */
    static authenticateUser(token,email){
        localStorage.setItem('token',token);
        localStorage.setItem('email',email);
    }
    /**
     * check if the user is authenticated
     */
    static isUserAuthenticated(){
        return localStorage.getItem('token') !== null;
    }
    /**
     * De-authenticate user log out
    */
    static deauenticate(){
        localStorage.removeItem('token');
        localStorage.removeItem('email');
    }

    /**
     * get a token value
     * load more news will use it
     */
    static getToken(){
        return localStorage.getItem('token');
    }

    /**
     * get email
     */
    static getEmail(){
        return localStorage.getItem('email');
    }
}

export default Auth;