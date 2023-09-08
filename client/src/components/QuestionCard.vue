<template>
  <a-card :title="currentQuestion.description">
    <template #extra><a href="#">1/12</a></template>
    <template #actions>
      <a-button v-on:click="onClickNext">Далее</a-button>
    </template>
    <a-checkbox-group v-model:value="value" style="width: 100%">
      <a-row>
        <a-col v-for="item of currentQuestion.answers" :key="item.id" :span="8">
          <a-checkbox :value=item.id>{{item.description}}</a-checkbox>
        </a-col>
      </a-row>
    </a-checkbox-group>
  </a-card>
</template>
  
  <script>
import { mapGetters } from 'vuex'
export default {
  name: "QuestionCard",
  props: {},
  data: () => ({
    question: {
    },
  }),
  computed: {
    ...mapGetters({
      currentQuestion: 'getCurrentQuestion'
    })
  },
  methods: {
    async onClickNext() {
      console.log("onClickTest");
      await this.$store.dispatch("nextQuestion");
    },
    // async setListData() {
    //   await this.$store.dispatch("getTestList");
    //   this.tests = this.$store.state.tests;
    // },
  },
  //   mounted(): ,
};
</script>
  <style >
.card {
  width: 100%;
  background-color: #e0e0e3;
  border-radius: 5px;
  text-align: left;
  border: 1px solid #e0e0e3;
}
</style>