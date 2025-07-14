import axios from 'axios';

export default {
  namespaced: true,
  state: {
    topScores: [],
    totalUsers: 0,
    quizCounts: [],
    attemptCounts: [],
  },

  mutations: {
    setTopScores(state, data) {
      state.topScores = data;
    },
    setTotalUsers(state, count) {
      state.totalUsers = count;
    },
    setQuizCounts(state, data) {
      state.quizCounts = data;
    },
    setAttemptCounts(state, data) {
      state.attemptCounts = data;
    },
  },

  actions:{
    async fetchAdminData({ commit }){
        const [scoresRes, usersRes] = await Promise.all([
          axios.get("http://localhost:5000/api/admin/top-scores"),
          axios.get("http://localhost:5000/api/admin/total-users"),
        ]);
        commit('setTopScores',scoresRes.data);
        commit('setTotalUsers',usersRes.data.count)
    },
    async fetchUserData( { commit }, user_id) {
        const res = await axios.get(
          `http://localhost:5000/api/user/${user_id}/quiz-stats`
        );
        commit('setQuizCounts', res.data.quizCount);
        commit('setAttemptCounts',res.data.attemptCount);
    }
  }
};