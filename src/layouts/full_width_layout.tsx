import { connect } from 'react-redux'
import Navbar from '../components/navigation/navbar';
import Footer from '../components/navigation/footer';
import Alert from '../components/alert/alert';
import { useEffect } from 'react';
import { get_network_id, loadWeb3 } from '../redux/actions/web3';
import { get_my_user_details } from '../redux/actions/user';
declare let window: any;

const FullWidthLayout = ({children, loadWeb3, get_network_id, my_user, get_my_user_details}:any) => {
  
  function handleChainChanged(_chainId:any) {
    // We recommend reloading the page, unless you must do otherwise
    window.location.reload();
  }

  if (window.ethereum) {
    window.ethereum.on("chainChanged", handleChainChanged);
  }

  useEffect(() => {
      const fetchData = async () => {
        if (localStorage.getItem("account")) {
          loadWeb3();
          my_user ? <></>:get_my_user_details()
        }
      };
      fetchData();

      if (window.ethereum) {
        get_network_id();
      }
  }, []);

  return (
    <div>
      <Navbar loading={false} />
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="max-w-7xl mx-auto">{children}</div>
        </div>
      <Footer/>
      <Alert/>
    </div>
  )
}

const mapStateToProps = (state: any) => ({

})

export default connect(mapStateToProps, {
  loadWeb3,
  get_network_id,
  get_my_user_details,
}) (FullWidthLayout);