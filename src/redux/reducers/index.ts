import { combineReducers } from "redux";
import alert from './alert'
import web3 from "./web3";

export default combineReducers({
    alert,
    web3
})