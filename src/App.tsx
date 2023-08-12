import { Provider } from "react-redux";
import store from "./store";
import NotFound from "./containers/errors/not_found";
import Home from "./containers/pages/home";
import { BrowserRouter, Route, Routes } from "react-router-dom";
import Connect from "./containers/pages/connect";
import VideoStream from "./containers/pages/video_stream";
import Cmath from "./containers/pages/cmath";

function App() {

  return (
    <Provider store={store}>
      <BrowserRouter>
          <Routes>
            <Route path="*" element={<NotFound/>}/>
            <Route path="/" element={<Home/>}/>
            <Route path="/video-stream" element={<VideoStream/>}/>
            <Route path="/cmath" element={<Cmath/>}/>
            <Route path="/connect" element={<Connect network={0} ethereum_balance={[]}/>}/>
          </Routes>
      </BrowserRouter>
    </Provider>
  );
}

export default App;
