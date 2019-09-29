import { Component, OnInit, SystemJsNgModuleLoader } from '@angular/core';
import { FormControl, FormBuilder, FormGroup} from '@angular/forms';
import { HttpClient } from '@angular/common/http';


@Component({
  selector: 'app-main',
  templateUrl: './main.component.html',
  styleUrls: ['./main.component.css']
})
export class MainComponent implements OnInit {

  //SERVER_URL = "https://us-central1-howrichdoyoulook.cloudfunctions.net/dbHit";
  SERVER_URL = "https://us-central1-howrichdoyoulook.cloudfunctions.net/faceToNum";
  url;
  imageVal = -1;
  budget = new FormControl('');
  uploadForm: FormGroup;


  //constructor() { }

  constructor(private formBuilder: FormBuilder, private httpClient: HttpClient) { }

  ngOnInit() {
    this.uploadForm = this.formBuilder.group({
      profile: ['']
    });
  }


  updateBudget() {
    console.log("this.budget: " + this.budget.value);
    //this.name.setValue('Nancy');

  }

  onFileSelect(event) {
    if (event.target.files.length > 0) {
      const file = event.target.files[0];
      this.uploadForm.get('profile').setValue(file);
    }
    if (event.target.files && event.target.files[0]) {
      var reader = new FileReader();

      reader.readAsDataURL(event.target.files[0]); // read file as data url

      reader.onload = (event) => { // called once readAsDataURL is completed
        let target: any = event.target; //<-- This (any) will tell compiler to shut up!
        let content: string = target.result;
        this.url = content;
      }
    }

    this.imageVal = Math.floor(Math.random() * Math.floor(5));

    console.log(this.imageVal.valueOf());
  }

  onSelectFile(event) { // called each time file input changes
    if (event.target.files && event.target.files[0]) {
      var reader = new FileReader();

      reader.readAsDataURL(event.target.files[0]); // read file as data url

      reader.onload = (event) => { // called once readAsDataURL is completed
        let target: any = event.target; //<-- This (any) will tell compiler to shut up!
        let content: string = target.result;
        this.url = content;
      }
    }

    this.imageVal = Math.floor(Math.random() * Math.floor(5));

    console.log(this.imageVal.valueOf());

    //console.log('' + this.url.value);

  }

  onSubmit() {
    const formData = new FormData();
    formData.append('file', this.uploadForm.get('profile').value);

    
  this.httpClient.post<any>(this.SERVER_URL, formData).subscribe(
      (res) => console.log(res),
      (err) => console.log(err)
    );

    
    

    // this.httpClient.post<any>(this.SERVER_URL, {number: 5}).subscribe(
    //   (res) => console.log(res),
    //   (err) => console.log(err)
    // );

    
  }


}
