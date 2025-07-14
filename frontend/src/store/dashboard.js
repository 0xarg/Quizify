import axios from 'axios';

export default {
  namespaced: true,
  state: {
    topScores: [],
    subjectAttempts: 0,
    quizCounts: [],
    attemptCounts: [],
  },

  mutations: {
    setTopScores(state, data) {
      state.topScores = data;
    },
    setSubjectAttempts(state, data) {
      state.subjectAttempts = data;
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
        const [scoresRes, attemptsRes] = await Promise.all([
          axios.get("http://localhost:5000/api/admin/top-scores"),
          axios.get("http://localhost:5000/api/admin/subject-attempts"),
        ]);
        commit('setTopScores',scoresRes.data);
        commit("setSubjectAttempts", attemptsRes.data);
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