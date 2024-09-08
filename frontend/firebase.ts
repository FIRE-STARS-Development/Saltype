import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";

const firebaseConfig = {
    apiKey: "AIzaSyCcJd4KXxMQiAHnEO1814vci7ngRNkPYwA",
    authDomain: "developmenttypingapplication.firebaseapp.com",
    projectId: "developmenttypingapplication",
    storageBucket: "developmenttypingapplication.appspot.com",
    messagingSenderId: "853345930052",
    appId: "1:853345930052:web:363bd660767dcd8c366511",
    measurementId: "G-F864BPQTQD"
};

const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);

export default app;