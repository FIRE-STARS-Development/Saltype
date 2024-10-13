import { describe, it, expect } from "vitest";
import { mount } from "@vue/test-utils";
import Textarea from "~/components/atoms/inputs/Textarea.vue";

describe("Textarea", () => {
  it("デフォルトpropsで正しくレンダリングされる", () => {
    const wrapper = mount(Textarea);
    const textarea = wrapper.find("textarea");
    expect(textarea.exists()).toBe(true);
    expect(textarea.attributes("id")).toBe("default");
    expect(textarea.classes()).toContain("input-text--white");
    expect(textarea.classes()).toContain("input-border--none");
    expect(textarea.classes()).toContain("input-width--medium");
    expect(textarea.classes()).toContain("input-height--medium");
    expect(textarea.classes()).toContain("input-background--black");
    expect(textarea.classes()).not.toContain("input--rounded");
  });

  it("カスタムpropsで正しくレンダリングされる", () => {
    const wrapper = mount(Textarea, {
      props: {
        id: "custom-textarea",
        placeholder: "Enter your message",
        required: true,
        color: "main-color",
        border: "sub-color",
        width: "large",
        height: "small",
        background: "white",
        rounded: true,
      },
    });
    const textarea = wrapper.find("textarea");
    expect(textarea.attributes("id")).toBe("custom-textarea");
    expect(textarea.attributes("placeholder")).toBe("Enter your message");
    expect(textarea.attributes("required")).toBe("");
    expect(textarea.classes()).toContain("input-text--main-color");
    expect(textarea.classes()).toContain("input-border--sub-color");
    expect(textarea.classes()).toContain("input-width--large");
    expect(textarea.classes()).toContain("input-height--small");
    expect(textarea.classes()).toContain("input-background--white");
    expect(textarea.classes()).toContain("input--rounded");
  });

  it("modelValueが正しく更新される", async () => {
    const wrapper = mount(Textarea, {
      props: {
        modelValue: "",
      },
    });
    const textarea = wrapper.find("textarea");
    await textarea.setValue("test value");
    expect(wrapper.emitted("update:modelValue")).toBeTruthy();
    expect(wrapper.emitted("update:modelValue")![0]).toEqual(["test value"]);
  });

  it.each([
    { input: "string value", expected: "string value" },
    { input: 123, expected: "123" },
    { input: ["array", "value"], expected: "array,value" },
    { input: null, expected: "" },
  ])("getStringValue関数が正しく動作する: %s", ({ input, expected }) => {
    const wrapper = mount(Textarea, {
      props: {
        modelValue: input,
      },
    });
    const textarea = wrapper.find("textarea");
    expect(textarea.element.value).toBe(expected);
  });

  it.each(["white", "black", "main-color", "sub-color"] as const)(
    "テキストカラー %s が正しく適用される",
    (color) => {
      const wrapper = mount(Textarea, {
        props: { color },
      });
      expect(wrapper.find("textarea").classes()).toContain(
        `input-text--${color}`
      );
    }
  );

  it.each(["white", "black", "main-color", "sub-color", "none"] as const)(
    "ボーダーカラー %s が正しく適用される",
    (border) => {
      const wrapper = mount(Textarea, {
        props: { border },
      });
      expect(wrapper.find("textarea").classes()).toContain(
        `input-border--${border}`
      );
    }
  );

  it.each(["small", "medium", "large"] as const)(
    "幅 %s が正しく適用される",
    (width) => {
      const wrapper = mount(Textarea, {
        props: { width },
      });
      expect(wrapper.find("textarea").classes()).toContain(
        `input-width--${width}`
      );
    }
  );

  it.each(["small", "medium", "large"] as const)(
    "高さ %s が正しく適用される",
    (height) => {
      const wrapper = mount(Textarea, {
        props: { height },
      });
      expect(wrapper.find("textarea").classes()).toContain(
        `input-height--${height}`
      );
    }
  );

  it.each(["white", "black", "main-color", "sub-color"] as const)(
    "背景色 %s が正しく適用される",
    (background) => {
      const wrapper = mount(Textarea, {
        props: { background },
      });
      expect(wrapper.find("textarea").classes()).toContain(
        `input-background--${background}`
      );
    }
  );
});