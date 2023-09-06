<template>
    <a-list
      item-layout="horizontal"
      :data-source="tests"
      :pagination="pagination"
    >
      <template #renderItem="{ item }">
        <a-list-item>
          <template #actions>
            <a key="list-loadmore-edit">Начать тест</a>
          </template>
          <a-list-item-meta>
            <template #title>
              <a href="https://www.antdv.com/">{{ item.name }}</a>
            </template>
          </a-list-item-meta>
          <div>{{item.description}}</div>
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
    tests: [
      { name: "222123", description: "qwe123123" },
      { name: "123", description: "qwe" },
      { name: "222123", description: "qwe123123" },
      { name: "123", description: "qwe" },
      { name: "222123", description: "qwe123123" },
      { name: "123", description: "qwe" },
      { name: "222123", description: "qwe123123" },
      { name: "123", description: "qwe" },
      { name: "222123", description: "qwe123123" },
      { name: "123", description: "qwe" },
      { name: "222123", description: "qwe123123" },
      { name: "123", description: "qwe" },
    ],
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

</style>