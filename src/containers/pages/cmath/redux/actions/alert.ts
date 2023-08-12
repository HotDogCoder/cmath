import { SET_ALERT, REMOVE_ALERT } from "./types";

export const set_alert = (msg:string, alert_type:string, timeout:number = 4000) => (dispatch:any) => {
    dispatch({
        type: SET_ALERT,
        payload: {
            msg,
            alert_type
        }
    }),
    setTimeout(() => 
        dispatch(
            {
                type: REMOVE_ALERT
            }
        ),
        timeout
    )
}