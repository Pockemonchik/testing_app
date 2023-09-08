<template>
  <a-card
    :bordered="false"
    :title="currentQuestion.description ? currentQuestion.description : ''"
  >
    <template #extra
      ><a href="#"
        >{{ currentQuestionIndex }} / {{ currentTestLength }}</a
      ></template
    >
    <template #actions>
      <a-button
        v-if="currentQuestionIndex == currentTestLength"
        @click="onClickResult"
        >Результат</a-button
      >
      <a-button v-else @click="onClickNext">Далее</a-button>
    </template>
    <a-checkbox-group v-model:value="checked" style="width: 100%">
      <a-row>
        <a-col
          v-for="item of currentQuestion.answers"
          :key="item.id"
          :span="16"
        >
          <a-checkbox
            @change="onCheckChange"
            :value="item.id"
            >{{ item.description }}</a-checkbox
          >
          <br />
          <br />
        </a-col>
      </a-row>
    </a-checkbox-group>
  </a-card>
</template>
  
  <script>
import { mapGetters } from "vuex";
import { ref } from "vue";
import { notification } from "ant-design-vue";
export default {
  name: "QuestionCard",
  props: {},
  data: () => ({
    answers: [],
    checked: ref([]),
  }),
  computed: {
    ...mapGetters({
      currentQuestion: "getCurrentQuestion",
      currentTestLength: "getCurrentTestLength",
      currentQuestionIndex: "getCurrentQuestionIndex",
    }),
  },
  methods: {
    async onClickNext() {
      console.log("onClickTest answers", this.answers);
      if (this.answers.length > 0) {
        await this.$store.dispatch("nextQuestion", this.answers);
        this.answers = [];
        return true;
      } else {
        notification["error"]({
          message: "Выберите один или несколько ответов!",
        });
        return false;
      }
    },
    async onClickResult() {
      let ready = await this.onClickNext();
      if (ready) {
        await this.$store.dispatch("getTestResult");
        notification["success"]({
          message: "Вы прошли тест!",
          description:
            "Правильных ответов: " +
            this.$store.state.testStats.correct_count +
            " | " +
            this.$store.state.testStats.correct_persent +
            " % !",
        });
      }
    },
    onCheckChange(e) {
      e.target.checked
        ? this.answers.push(e.target.value)
        : (this.answers = this.answers.filter(
            (item) => item != e.target.value
          ));
    },
  },
};
</script>
  <style >
</style>