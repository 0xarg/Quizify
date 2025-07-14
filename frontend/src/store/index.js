import { createStore } from 'vuex'
import dashboard from './dashboard';

const store = createStore({
  state: {
    auth_token:null,
    roles: [],
    loggedIn: false,
    user_id: null,
    username:'',

  },
  getters: {
  },
  mutations: {

    setUser(state){
      try{
        if (JSON.parse(localStorage.getItem("user"))) {
          const user = JSON.parse(localStorage.getItem("user"));
          state.auth_token = user.token;
          state.roles  = user.roles;
          state.loggedIn = true;
          state.username = user.email?.split("@")[0] || "User";
          state.user_id = user.id;
        }
      } catch{
        console.warn("User not Logged In")
      }
    },
        
    logout(state){
      state.auth_token=null;
      state.roles = [];
      state.loggedIn = false;
      state.user_id = null;

      localStorage.removeItem("user")

    }
  },



  actions: {
  },
  modules: {
    dashboard
  }
})
store.commit("setUser");
export default store;
