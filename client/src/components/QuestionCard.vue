<template>
  <a-card :title="question.description">
    <template #extra><a href="#">1/12</a></template>
    <template #actions>
      <a-button>Отправить</a-button>
    </template>
    <a-checkbox-group v-model:value="value" style="width: 100%">
      <a-row>
        <a-col v-for="item of question.answers" :key="item" :span="8">
          <a-checkbox value="A">{{item}}</a-checkbox>
        </a-col>
      </a-row>
    </a-checkbox-group>
  </a-card>
</template>
  
  <script>
export default {
  name: "QuestionCard",
  props: {},
  data: () => ({
    question: {
      description: "Вопрос 1",
      answers: ["1 ответ", "2 ответ", "3 ответ", "4 ответ"],
    },
  }),

  methods: {
    onClickTest(values) {
      console.log("Success:", values, this.$store.state);
      //   await this.$store.dispatch("auth", values);;
    },
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