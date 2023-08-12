import {
    LOAD_ETHEREUM_BALANCE_SUCCESS,
    LOAD_ETHEREUM_BALANCE_FAIL,
    LOAD_WEB3_SUCCESS,
    LOAD_WEB3_FAIL,
    LOAD_NETWORK_SUCCESS,
    LOAD_NETWORK_FAIL,
    SET_LOADING,
} from '../actions/types'
import { Web3Account } from '../interfaces/web3_account'

const initialState: Web3Account = {
    account: null,
    network: 0,
    ethereum_balance: [],
    loading: false,
    my_user: null
};

export default function web3(state = initialState, action:any) {
    const { type, payload } = action;

    switch (type) {
        case LOAD_NETWORK_SUCCESS:
            return {
                ...state,
                network: payload,
            };
        case LOAD_WEB3_SUCCESS:
            return {
                ...state,
                account: payload,
            };
        case LOAD_WEB3_FAIL:
            return {
                ...state,
                web3: null,
            };
        case LOAD_NETWORK_FAIL:
            return {
                ...state,
                network: null,
            };
        case LOAD_ETHEREUM_BALANCE_SUCCESS:
            return {
                ...state,
                ethereum_balance: payload,
            };
        case LOAD_ETHEREUM_BALANCE_FAIL:
            return {
                ...state,
                ethereum_balance: null,
            };
        case SET_LOADING:
            return {
                ...state,
                loading: payload,
            };
        default:
            return state;
    }
}