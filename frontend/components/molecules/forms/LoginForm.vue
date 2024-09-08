<script setup lang="ts">
import { ref } from "vue";
import { useRouter } from "vue-router";
import Input from "~/components/atoms/inputs/Input.vue";
import Button from "~/components/atoms/buttons/Button.vue";
import Image from "~/components/atoms/imgs/Image.vue";
import Field from "./ValidateField.vue";
import { Form } from "vee-validate";
import * as yup from "yup";
import { saveToken } from "~/composables/token";

import EyeRegular from "~/assets/images/index/eye-regular.svg";
import EyeSlashRegular from "~/assets/images/index/eye-slash-regular.svg";

const eyeRegular = ref(EyeRegular);
const eyeSlashRegular = ref(EyeSlashRegular);

const email = ref("");
const password = ref("");
const showPassword = ref(false);
const router = useRouter();

const passVisibility = () => {
  showPassword.value = !showPassword.value;
};

const validationSchema = yup.object().shape({
  email: yup.string().required().email().label("メールアドレス"),
  password: yup.string().required().min(8).label("パスワード"),
});

const handleSubmit = async () => {
  try {
    const response = await fetch("http://localhost:8000/api/login/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        email: email.value,
        password: password.value,
      }),
    });

    if (!response.ok) {
      alert("ログインに失敗しました。");
    }

    const data = await response.json();

    console.log(data.token);
    console.log(data.userName);

    saveToken(data.token);

    console.log(getToken());

    router.push({ name: "home" });
  } catch (error) {
    alert(
      "エラーが発生しました。ネットワークに接続されているか確認してください"
    );
  }
};
</script>

<template>
  <Form
    :validation-schema="validationSchema"
    v-slot="{ meta: { valid } }"
    @submit="handleSubmit"
  >
    <Field v-model="email" name="email" class="field">
      <template #input="{ field }">
        <Input
          type="email"
          id="email"
          v-bind="field"
          placeholder="&nbsp;メールアドレス"
          border="blue"
          width="large"
          :rounded="true"
        />
      </template>
    </Field>

    <Field v-model="password" name="password" class="field">
      <template #input="{ field }">
        <span>
          <Input
            :type="showPassword ? 'text' : 'password'"
            id="password"
            v-bind="field"
            placeholder="&nbsp;パスワード"
            border="blue"
            width="large"
            :rounded="true"
          />
          <Image
            v-if="showPassword"
            :image-src="eyeSlashRegular"
            alt="パスワード表示"
            width="mini"
            height="mini"
            class="eye"
            @click="passVisibility"
          />
          <Image
            v-else
            :image-src="eyeRegular"
            alt="パスワード非表示"
            width="mini"
            height="mini"
            class="eye"
            @click="passVisibility"
          />
        </span>
      </template>
    </Field>

    <div class="buttons">
      <Button
        type="reset"
        button-text="リセット"
        border="blue"
        :rounded="true"
      />
      <Button
        type="submit"
        button-text="ログイン"
        border="blue"
        :rounded="true"
        :disabled="!valid"
      />
    </div>
  </Form>
</template>

<style lang="scss" src="@/assets/styles/components/molecules/login-form.scss" />
