<template>
   <a-button v-on:click="logout">Выход</a-button>
  <div class="container">
    <a-row>
    <a-col :span="10"> <TestingList /></a-col>
    <a-col :span="10" :offset="2"><QuestionCard/></a-col>
  </a-row>
  </div>
</template>
  
<script>
import TestingList from "./TestingList.vue";
import QuestionCard from "./QuestionCard.vue";

export default {
  name: "TestingPage",
  components: {TestingList,QuestionCard},
  props: {},
  data: () => ({}),
  methods: {
    logout() {
      console.log("logout");
      this.$store.dispatch("logout");
      this.$router.push({ 
        path: 'auth',
    });
    },
  },
};
</script>
  
<style>
.container {
  height: 80vh;
  margin: 10px 10px 10px 10px;
  border-radius: 5px;
  margin-top: 5%;
  text-align: left;
  border: 1px solid #e0e0e3;
}
</style>
  