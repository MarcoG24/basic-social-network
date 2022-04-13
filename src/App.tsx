import './App.css';
import { BrowserRouter, Route, Routes } from 'react-router-dom'
import Login from './components/AuthUser/Login';
import { FC } from 'react';

const App: FC = () => (
<>
<BrowserRouter>
  <Routes>
    <Route path="*" element={<Login />} />
  </Routes>
</BrowserRouter>
</>
)
export default App