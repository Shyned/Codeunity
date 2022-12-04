import React from "react";
import ReactDOM from "react-dom/client";
import { createBrowserRouter, RouterProvider, Route } from "react-router-dom";
//pages
import Landing_Page from "./assets/routes/Landing_Page/Landing_Page";
import Chatroom_Page from "./assets/routes/Chatroom_Page/Chatroom_Page";
import Home_Page from "./assets/routes/Home_Page/Home_Page";
import SignUp_Page from "./assets/routes/Signup_Page/SignUp_Page";
import Login_Page from "./assets/routes/Login_Page/Login_Page";

const router = createBrowserRouter([
  {
    path: "/",
    element: <Landing_Page />,
  },
  { path: "chatroom/", element: <Chatroom_Page /> },
  { path: "home/", element: <Home_Page /> },
  { path: "login/", element: <Login_Page /> },
  { path: "signup/", element: <SignUp_Page /> },
]);

ReactDOM.createRoot(document.getElementById("root")).render(
  <React.StrictMode>
    <RouterProvider router={router} />
  </React.StrictMode>
);
