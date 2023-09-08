<template>
  <a-list
    item-layout="horizontal"
    :data-source="tests"
    :pagination="pagination"
  >
    <template #renderItem="{ item }">
      <a-list-item>
        <template #actions>
          <a key="list-loadmore-edit" v-on:click="onClickTest(item.id)"
            >Начать тест</a
          >
        </template>
        <a-list-item-meta>
          <template #title>
            <a href="">{{ item.theme }}</a>
          </template>
        </a-list-item-meta>
        <div>{{ item.description }}</div>
      </a-list-item>
    </template>
  </a-list>
</template>
  
  <script>
export default {
  name: "TestingList",
  props: {},
  data: () => ({
    pagination: {
      pageSize: 8,
    },
    tests: [],
  }),
  
  methods: {
    async onClickTest(id) {
      console.log("onClickTest");
      await this.$store.dispatch("getTest", id );
    },
    async setListData() {
      await this.$store.dispatch("getTestList");
      this.tests = this.$store.state.tests;
    },
  },

  mounted() {
    this.setListData();
  },
};
</script>
  <style >
</style>