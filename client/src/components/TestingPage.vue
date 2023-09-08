<template>
  <div class="bg-auth">
   <a-button v-on:click="logout" style="margin-top: 10px;">Выход</a-button>
    <a-row>
    <a-col :span="8"> <div class="container"><TestingList /></div></a-col>
    <a-col :span="16"><div class="container"><QuestionCard/></div></a-col>
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
.bg-auth {
  color: #f6f7fb;
  background-color: rgba(238, 236, 236, 0.8);
  height: 100vh;
  width: 100vw;
}

.container {
  height: 80vh;
  background-color: #ffffff;
  margin: 10px 10px 10px 10px;
  border-radius: 5px;
  text-align: left;
  border: 1px solid #e0e0e3;
}
</style>
  