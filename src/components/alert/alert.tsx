import { Fragment } from 'react'
import { connect } from 'react-redux'
import { HiAcademicCap } from 'react-icons/hi';

function Alert ({alert}:{alert:any}) {
    const display_alert = () => {
        if(alert !== null){
            return (
                <div className="bg-indigo-600 fixed z-50 bottom-0 inset-x-0 pb-2 sm:pb-5">
                    <div className="mx-auto max-w-7xl py-3 px-3 sm:px-6 lg:px-8">
                        <div className="flex flex-wrap items-center justify-between">
                            <div className="flex w-0 flex-1 items-center">
                                <span className={`flex rounded-lg bg-${alert.alert_type} p-2`}>
                                <HiAcademicCap/>
                                </span>
                                <p className="ml-3 truncate font-medium text-white">
                                <span className="md:hidden">We announced a new product!</span>
                                <span className="hidden md:inline">Big news! We're excited to announce a brand new product.</span>
                                </p>
                            </div>
                            <div className="order-3 mt-2 w-full flex-shrink-0 sm:order-2 sm:mt-0 sm:w-auto">
                                <a href="http://www.w3.org/2000/svg" className="flex items-center justify-center rounded-md border border-transparent bg-white px-4 py-2 text-sm font-medium text-indigo-600 shadow-sm hover:bg-indigo-50">Learn more</a>
                            </div>
                            <div className="order-2 flex-shrink-0 sm:order-3 sm:ml-3">
                                <button type="button" className="-mr-1 flex rounded-md p-2 hover:bg-indigo-500 focus:outline-none focus:ring-2 focus:ring-white sm:-mr-2">
                                <span className="sr-only">Dismiss</span>
                                <svg className="h-6 w-6 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" aria-hidden="true">
                                    <path stroke-linecap="round" stroke-linejoin="round" d="M6 18L18 6M6 6l12 12" />
                                </svg>
                                </button>
                            </div>
                        </div>
                    </div>
                </div>
            )
        } else {
            return <Fragment></Fragment>
        }
    }

     return <Fragment>{display_alert()}</Fragment>
}

const mapStateToProps = (state:any) => ({
    alert: state.alert.alert
})

export default connect(mapStateToProps)(Alert);