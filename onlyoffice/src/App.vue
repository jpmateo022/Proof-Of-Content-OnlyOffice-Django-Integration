
learlea<template>
  <div v-if="config.token != null">
    <DocumentEditor 
        id="docEditor" 
        :documentServerUrl="documentServerUrl"
        :config="config"
        :events_onDocumentReady="onDocumentReady" 
        :events_onDocumentStateChange="onDocumentStateChange"
    /> 
  </div>
</template>
<script>
import { DocumentEditor } from "@onlyoffice/document-editor-vue";
import axios from 'axios';

export default{
  components:{
    DocumentEditor
  },
  mounted(){
    
    this.getJWTToken()
  },
  methods: {
    onDocumentStateChange(data){
      console.log(data)
    },
    onDocumentReady() {
        console.log("Document is loaded");
    },
    getJWTToken(){
      return axios.post("http://localhost:7081/onlyoffice/payload/",{
          "config": JSON.stringify({
            "document": this.config.document,
            "height": this.config.height,
            "editorConfig": this.config.editorConfig
          })
      }
      
      ).then((response)=>{
        let data = response.data;
        this.config.token = data["token"];
      })
    },
    getCSRFToken(){
      return axios.get("http://localhost:7081/onlyoffice/csrf-token/").then((response)=>{
      let data = response.data;
      this.csrf_token = data["token"];
    })
    }    
  },
  data(){
    return {
      csrf_token: "",
      message: "Hello World",
      documentServerUrl:"http://localhost:6080/",
      config: {
        document: {
            permissions:{
              edit: true,
            },
            fileType: "docx",
            key: "Khirz6zTPdfd7",
            title: "LOREM IPSUM.docx",
            url: "http://host.docker.internal:6080/example/download?fileName=LOREM IPSUM.docx"
        },
        token: null,
        height:"1000px;",
        documentType: "word",
        editorConfig: {
            callbackUrl: "http://host.docker.internal:7081/onlyoffice/callback/"
        }
      }
    }
  }
}
</script>