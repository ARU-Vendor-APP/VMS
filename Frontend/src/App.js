import React from "react";
import "./App.css";
//import "./tailwind.output.css";
import { BrowserRouter as Router, Switch, Route } from "react-router-dom";
import LandingPage from "./pages/public/LandingPage";
import SignIn from "./pages/public/SignIn";
import SignUp from "./pages/public/SignUp";
import ForgotPassword from "./pages/public/ForgotPassword";
import ResetPassword from "./pages/public/ResetPassword";
import AcceptInvite from "./pages/public/AcceptInvite";
import AuthenticatedApp from "./AuthenticatedApp";
import { useAuth } from "./lib/authHandler";
import { Toaster } from "react-hot-toast";
import ProductDetails from "./pages/public/ProductDetails";

const App = () => {
  const { isAuthenticated, user } = useAuth();

  return (
    <div>
      {/* {isAuthenticated === true && user && <AuthenticatedApp />} */}
      {<AuthenticatedApp />}
      {/* {isAuthenticated === false && (
        <Router>
          <Switch>
            <Route path="/signin">
              <SignIn />
            </Route>
            <Route path="/signup">
              <SignUp />
            </Route>
            <Route path="/forgot_password">
              <ForgotPassword />
            </Route>
            <Route path="/reset_password/:token" children={<ResetPassword />} />
            <Route path="/invite/:token" children={<AcceptInvite />} />
            <Route path="/products/:id" children={<ProductDetails />} />
            <Route path="/">
              <LandingPage />
            </Route>
          </Switch>
        </Router>
      )}
      <Toaster /> */}
    </div>
  );
};

export default App;
