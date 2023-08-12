import axios from "axios";

const handleSubmitTestLandingPage = (handleFormSubmit: (data:any) => void, requestData: any) => {
axios.post(process.env.REACT_APP_API_URL+'/api/qa/qa-test/test-landing-page', requestData)
    .then((response:any) => {
    console.log(response.data);
    handleFormSubmit(response.data);
    })
    .catch(error => {
    console.log(error);
    });
};

const handleSubmitTestNotAuthMenuHamburguesa = (handleFormSubmit: (data:any) => void, requestData: any) => {
axios.post(process.env.REACT_APP_API_URL+'/api/qa/qa-test/test-not-auth-menu-hamburguesa', requestData)
    .then(response => {
    console.log(response.data);
    handleFormSubmit(response.data);
    })
    .catch(error => {
    console.log(error);
    });
};

const handleSubmitTestNotAuthMenuHamburguesaCol = (handleFormSubmit: (data:any) => void, requestData: any) => {
axios.post(process.env.REACT_APP_API_URL+'/api/qa/qa-test/test-not-auth-menu-hamburguesa-col', requestData)
    .then(response => {
    console.log(response.data);
    handleFormSubmit(response.data);
    })
    .catch(error => {
    console.log(error);
    });
};

const handleSubmitTestNotAuthMenuHamburguesaAd = (handleFormSubmit: (data:any) => void, requestData: any) => {
axios.post(process.env.REACT_APP_API_URL+'/api/qa/qa-test/test-not-auth-menu-hamburguesa-ad', requestData)
    .then(response => {
    console.log(response.data);
    handleFormSubmit(response.data);
    })
    .catch(error => {
    console.log(error);
    });
};

const handleSubmitTestNotAuthPromociones = (handleFormSubmit: (data:any) => void, requestData: any) => {
axios.post(process.env.REACT_APP_API_URL+'/api/qa/qa-test/test-not-auth-promociones', requestData)
    .then(response => {
    console.log(response.data);
    handleFormSubmit(response.data);
    })
    .catch(error => {
    console.log(error);
    });
};

const handleSubmitTestQuienesSomos = (handleFormSubmit: (data:any) => void, requestData: any) => {
axios.post(process.env.REACT_APP_API_URL+'/api/qa/qa-test/test-quienes-somos', requestData)
    .then(response => {
    console.log(response.data);
    handleFormSubmit(response.data);
    })
    .catch(error => {
    console.log(error);
    });
};

const handleSubmitTestLoginCol = (handleFormSubmit: (data:any) => void, requestData: any) => {
axios.post(process.env.REACT_APP_API_URL+'/api/qa/qa-test/test-login-col', requestData)
    .then(response => {
    console.log(response.data);
    handleFormSubmit(response.data);
    })
    .catch(error => {
    console.log(error);
    });
};

const handleSubmitTestLoginAd = (handleFormSubmit: (data:any) => void, requestData: any) => {
axios.post(process.env.REACT_APP_API_URL+'/api/qa/qa-test/test-login-ad', requestData)
    .then(response => {
    console.log(response.data);
    handleFormSubmit(response.data);
    })
    .catch(error => {
    console.log(error);
    });
};

const handleSubmitTestLoginInGames = (handleFormSubmit: (data:any) => void, requestData: any) => {
axios.post(process.env.REACT_APP_API_URL+'/api/qa/qa-test/test-login-in-games', requestData)
    .then(response => {
    console.log(response.data);
    handleFormSubmit(response.data);
    })
    .catch(error => {
    console.log(error);
    });
};