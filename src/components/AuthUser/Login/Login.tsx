import { FC } from "react";
import { Button, Form } from 'react-bootstrap';
import './Login.css'

const Login: FC = () => (
  
    // console.log('Connected to PlanetScale!');
    // console.log(process.env.REACT_APP_DATABASE_URL)
  
    // const mysql = require('mysql2');
    // const connection = mysql.createConnection(process.env.REACT_APP_DATABASE_URL);
    // console.log('Connected to PlanetScale!');
    // connection.end();
    <div className="wrapper fadeInDown">
  <div id="formContent">
    {/* <!-- Tabs Titles --> */}

    {/* <!-- Ickon --> */}
    <div className="fadeIn first">
      <img src="http://danielzawadzki.com/codepen/01/icon.svg" id="icon" alt="User Icon" />
    </div>

    {/* <!-- Login Form --> */}
    <Form>
  <Form.Group className="mb-3" controlId="formBasicEmail">
    <Form.Label>Email address</Form.Label>
    <Form.Control type="email" className="fadeIn second" placeholder="Enter email" />
  </Form.Group>

  <Form.Group className="mb-3" controlId="formBasicPassword">
    <Form.Label>Password</Form.Label>
    <Form.Control type="password" placeholder="Password" />
  </Form.Group>
  <Form.Group className="mb-3" controlId="formBasicCheckbox">
    <Form.Check type="checkbox" label="Check me out" />
  </Form.Group>
  <Button variant="primary" className="fadeIn fourth" type="submit">
    Submit
  </Button>
</Form>

    {/* <!-- Remind Passowrd --> */}
    <div id="formFooter">
      <a className="underlineHover" href="#">Forgot Password?</a>
    </div>

  </div>
</div>
  

    )
  
  export default Login;