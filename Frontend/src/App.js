import React from "react";
import "./App.css";
import { BrowserRouter as Router, Switch, Route } from "react-router-dom";
import LandingPage from "./pages/public/LandingPage";
import AuthenticatedApp from "./AuthenticatedApp";
import { useAuth } from "./lib/authHandler";
import { Toaster } from "react-hot-toast";

const App = () => {
  const { isAuthenticated, user } = useAuth();

  return (
    <div>
      {/* {isAuthenticated === true && user && <AuthenticatedApp />} */}
      {/* {<AuthenticatedApp />} */}
      {isAuthenticated === false && (
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
            <Route path="/">
              <LandingPage />
            </Route>
          </Switch>
        </Router>
      )}
      <Toaster />
    </div>
  );
};

export default App;
