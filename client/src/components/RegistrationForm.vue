<template>
    <div class="bg">
      <div class="authBox">
        <div class="reg-card">
          <a-divider>Регистрация</a-divider>
          <div className="form">
            <a-form
              :model="formState"
              name="basic"
              autocomplete="off"
              @finish="onFinish"
              @finishFailed="onFinishFailed"
            >
              <a-form-item
              :label-col="{ span: 10 }"
              :wrapper-col="{ span: 14 }"
                label="Логин"
                name="username"
                :rules="[
                  { required: true, message: 'Please input your username!' },
                ]"
              >
                <a-input v-model:value="formState.username">
                  <template #prefix>
                    <UserOutlined class="site-form-item-icon" />
                  </template>
                </a-input>
              </a-form-item>
  
              <a-form-item
                label="Пароль"
                name="password"
                :label-col="{ span: 10 }"
              :wrapper-col="{ span: 14 }"
                :rules="[
                  { required: true, message: 'Please input your password!' },
                ]"
              >
                <a-input-password v-model:value="formState.password">
                  <template #prefix>
                    <LockOutlined class="site-form-item-icon" />
                  </template>
                </a-input-password>
              </a-form-item>
              <a-form-item
                label="Повторите"
                name="confirm"
                :label-col="{ span: 10 }"
              :wrapper-col="{ span: 14 }"
                :rules="[
                  { required: true, message: 'Please input your password!' },
                ]"
              >
                <a-input-password v-model:value="formState.confirm">
                  <template #prefix>
                    <LockOutlined class="site-form-item-icon" />
                  </template>
                </a-input-password>
              </a-form-item>
              <a-form-item>
                
                <a-button type="primary" html-type="submit" class="login-form-button">Зарегистрироваться</a-button>
                <a-divider></a-divider>
                <router-link  to="/auth">Авторизация</router-link>
              </a-form-item>
            </a-form>
          </div>
        </div>
      </div>
    </div>
  </template>
  
    <script>
  export default {
    name: "RegistrationForm",
    props: {},
    data: () => ({
      formState: {
        username: "",
        password: "",
        confirm:"",
      },
    }),
    methods: {
      async onFinish(values) {
        await this.$store.dispatch("registration", values);
        console.log("Success:", values, this.$store.state);
        await this.$router.push({path: 'testing'})
      },
      onFinishFailed(errorInfo) {
        console.log("Failed:", errorInfo);
      },
    },
  };
  </script>
  
  <style>
  .bg {
    color: #f6f7fb;
    background-color: rgba(238, 236, 236, 0.8);
    height: 100%;
    width: 100vw;
  }
  
  .authBox {
    display: flex;
    flex-direction: column;
    align-items: center;
    height: 100vh;
  }
  
  .reg-card {
    width: 350px;
    background-color: #ffffff;
    border-radius: 5px;
    margin-top: 5%;
    text-align: center;
    border: 1px solid #e0e0e3;
  }
  
  .form {
    padding: 20px 20px 0;
  }
  
  .login-form-button {
    width: 90%;
    margin-left: 10px;
    margin-right: 10px;
  }
  </style>