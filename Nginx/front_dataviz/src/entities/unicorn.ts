export class Unicorn {
    private _nom: string;
    private _description: string;
    private _image: string;
    private _rank: number;
    private _price: number;
    private _type: string;

    public constructor(nom :string, description :string, image :string, rank :number, price :number, type :string) {
        this._nom = nom;
        this._description = description;
        this._image = image;
        this._rank = rank;
        this._price = price;
        this._type = type;
    }


    get nom(): string {
        return this._nom;
    }

    set nom(value: string) {
        this._nom = value;
    }

    get description(): string {
        return this._description;
    }

    set description(value: string) {
        this._description = value;
    }

    get image(): string {
        return this._image;
    }

    set image(value: string) {
        this._image = value;
    }

    get rank(): number {
        return this._rank;
    }

    set rank(value: number) {
        this._rank = value;
    }

    get price(): number {
        return this._price;
    }

    set price(value: number) {
        this._price = value;
    }

    get type(): string {
        return this._type;
    }

    set type(value: string) {
        this._type = value;
    }
}