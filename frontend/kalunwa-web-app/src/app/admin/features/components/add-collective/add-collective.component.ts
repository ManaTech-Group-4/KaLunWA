import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { MatSnackBar } from '@angular/material/snack-bar';
import { ActivatedRoute, Router } from '@angular/router';
import { CollectivePagesService } from '../../service/collective-pages.service';

@Component({
  selector: 'app-add-collective',
  templateUrl: './add-collective.component.html',
  styleUrls: ['./add-collective.component.scss']
})
export class AddCollectiveComponent implements OnInit {
  collective: FormGroup;
  submitted= false;
  collectiveType: string | null= "project";
  fileName="";
  collection:any;
  profileImage:string;

  constructor(
    private formBuilder: FormBuilder,
    private service: CollectivePagesService,
    private route: ActivatedRoute,
    private router: Router,
    private snackBar: MatSnackBar
  ) { }

  ngOnInit(): void {
      this.collective = this.formBuilder.group({
      title: ['',Validators.required],
      start_date: [null],
      end_date: [null],
      camp: [''],
      description: ['',Validators.required],
      meta_description: [''],
      image:[null]
    });

    this.collectiveType = this.route.snapshot.paramMap.get("collective-type");
    this.profileImage = "../../assets/images/place.jpg";
  }

  get f() { return this.collective.controls;}

  onSubmit(imageInput:any){
    this.submitted = true;

    console.log(this.collective);

    if(this.collective.invalid){
      return;
    }
    if(this.collectiveType != 'announcement')
      this.processFile(imageInput);
    else
      this.createCollective(0);
  }

  private createCollective(id:number){
    console.log(this.collectiveType);
    let newItem: any;
    if(this.collectiveType != 'news' && this.collectiveType != 'announcement')
      newItem = {
        'title': this.f.title.value,
        'start_date': this.f.start_date.value,
        'end_date': this.f.end_date.value,
        'camp': this.f.camp.value,
        'description': this.f.description.value,
        'image': id
      };

    else if(this.collectiveType == 'news')
      newItem = {
        'title': this.f.title.value,
        'description': this.f.description.value,
        'image': id
      };

    else if(this.collectiveType == 'announcement')
    newItem = {
      'title': this.f.title.value,
      'description': this.f.description.value,
      'meta_description': this.f.meta_description.value
    };


    if(this.collectiveType=="project"){
      const addSubscribe = this.service.addProject(newItem).subscribe(
        suc => {
          console.log('success');
          this.router.navigateByUrl("admin/collective");
          this.snackBar.open(`Successfully created a new ${this.collectiveType}`, `Close`, {duration: 5000});
          addSubscribe.unsubscribe;
        },
        err => {
          console.log(err);
        }
      );
    }
    if(this.collectiveType=="event"){
      const addSubscribe = this.service.addEvent(newItem).subscribe(
        suc => {
          console.log('success');
          this.router.navigateByUrl("admin/collective");
          this.snackBar.open(`Successfully created a new ${this.collectiveType}`, `Close`, {duration: 5000});
          addSubscribe.unsubscribe;
        },
        err => {
          console.log(err);
        }
      );
    }
    if(this.collectiveType=="news"){
      const addSubscribe = this.service.addNews(newItem).subscribe(
        suc => {
          console.log('success');
          this.router.navigateByUrl("admin/collective");
          this.snackBar.open(`Successfully created a new ${this.collectiveType}`, `Close`, {duration: 5000});
          addSubscribe.unsubscribe;
        },
        err => {
          console.log(err);
        }
      );
    }
    if(this.collectiveType=="announcement"){
      const addSubscribe = this.service.addAnnoucement(newItem).subscribe(
        suc => {
          console.log('success');
          this.router.navigateByUrl("admin/collective");
          this.snackBar.open(`Successfully created a new ${this.collectiveType}`, `Close`, {duration: 5000});
          addSubscribe.unsubscribe;
        },
        err => {
          console.log(err);
        }
      );
    }
  }

  onFileChange(imageInput:any){
    const file: File = imageInput.target.files[0];
    const reader = new FileReader();
    if(!this.isFileImage(file))
      this.collective.controls["image"].setErrors({'incorrect': true});
    else{
      this.collective.controls["image"].setErrors(null);

      this.fileName = file.name;
    }


    if(imageInput.target.files && imageInput.target.files[0]){
      // File Preview
      reader.readAsDataURL(file);

      reader.onload = () => {
        this.profileImage = reader.result as string;
      }
    }
  }

  processFile(imageInput: any) {
    const file: File = imageInput.files[0];
    const reader = new FileReader();

    if(this.isFileImage(file)){

      reader.addEventListener('load', (event: any) => {

        this.service.uploadImage(this.fileName,file).subscribe(
          (res:any) => {
            this.createCollective(res.id);

          },
          (err) => {
            console.log("Err");
          })
        });

        reader.readAsDataURL(file);
    }
  }

  isFileImage(file: File) {
    return file && file['type'].split('/')[0] === 'image';
  }

  displayDate(date: Date){
    if(!date)
      return "";
    return this.service.printDate(date);
  }


}
