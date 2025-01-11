import { createStore } from 'vuex'

const store = createStore({
  state: {
    auth_token:null,
    roles: [],
    loggedIn: false,
    user_id: null,

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
          state.user_id = user.id;
        }
      } catch{
        console.warn("User not Logged In")
      }
    },
        
    logout(state){
      auth_token:null;
      roles: [];
      loggedIn: false;
      user_id: null;

      localStorage.removeItem("user")

    }
  },



  actions: {
  },
  modules: {
  }
})
store.commit("setUser");
export default store;
